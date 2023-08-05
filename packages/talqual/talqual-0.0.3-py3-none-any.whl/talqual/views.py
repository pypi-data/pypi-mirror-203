import functools
import logging
from pathlib import Path

from anytree import Node
from anytree.resolver import ChildResolverError, Resolver

from .importer import File
from .parsers.html import contains_id, get_all_href


log = logging.getLogger('talqual')


def hardlink_to(dst_path, src_path):
    """Different hardlinking order in diferrent Python versions"""
    try:
        dst_path.hardlink_to(src_path)  # pragma: py-gte-39
    except AttributeError:
        src_path.link_to(dst_path)  # pragma: py-lt-39


class View(Node):
    """A rendered `Template` with data

    * self.value: File contents
    """

    def relative_path(self):
        return self.separator.join([str(node.name) for node in self.path[1:]])

    def _write_hardlink(self, src_path, dst_path):
        try:
            hardlink_to(dst_path, src_path)
        except FileExistsError:
            src_inode = src_path.stat().st_ino
            dst_inode = dst_path.stat().st_ino
            if src_inode != dst_inode:
                # file has changed
                dst_path.unlink()
                hardlink_to(dst_path, src_path)

    def _write_contents(self, directory):
        """
        :type directory: `Path`
        """
        # if 'value' not in self.__dict__:
        #    return

        path = directory.joinpath(self.relative_path())

        if isinstance(self.value, File):
            original_path = self.value.path
            self._write_hardlink(original_path, path)
        elif isinstance(self.value, bytes):
            path.write_bytes(self.value)
        else:
            path.write_text(self.value)

    def _write_folder(self, directory):
        """
        :type directory: `Path`
        """
        if self.is_root:
            pass
        path = directory.joinpath(self.relative_path())
        if not path.exists():
            path.mkdir()

    def write(self, directory='html'):
        """
        :type directory: `Path` or `str`
        """
        directory = Path(directory)
        if self.is_leaf:
            self._write_contents(directory)
        else:
            self._write_folder(directory)

        for child in self.children:
            child.write(directory)

    def check_broken_links(self):
        """
        :return: number of errors
        :rtype: int
        """
        errors = 0
        for child in self.children:
            errors += child.check_broken_links()
        return errors


class CollectionView(View):
    """A collection of `Views` that get rendered directly on parent"""
    pass


class ViewHtml(View):
    """A rendered HTML `Template`"""
    def check_broken_links(self):
        """Check that all links inside the HTML document point to an existing url

        Prints the offending links.

        :return: number of errors
        :rtype: int
        """
        errors = super().check_broken_links()

        hrefs = get_all_href(self.value)

        # check internal
        internal = 0
        external = 0
        errors_internal = 0
        for dst, url, fragment in hrefs:
            if dst == 'internal':
                internal += 1
                if self.is_broken_link_internal(url, fragment):
                    errors_internal += 1
            elif dst == 'external':
                external += 1
                # check external
                # should check optionally, because HEAD http requests slow
                # should check with memoize

        log_i = f'Broken internal {errors_internal}/{internal}. '
        log_e = f'External {external}: all not checked.'
        log.debug(f'Checked links in {self.relative_path()}. ' + log_i + log_e)

        return errors+errors_internal

    def is_broken_link_internal(self, url, fragment):
        """Check that internal link `url`#`fragment` inside the HTML document
        point to an existing document.

        Prints the offending internal links.

        :return: Is the link broken?
        :rtype: bool
        """
        if url in ('.', ''):
            node_search = self
        else:
            node_search = self.parent

        if url.startswith('/'):
            # must include root name
            url = f'/{self.root.name}{url}'

        # check url
        path = self.relative_path()
        resolver = Resolver('name')
        try:
            node = resolver.get(node_search, url)
        except (AttributeError, ChildResolverError):
            log.warning(f'Broken internal link {url} in {path}')
            return True

        # check fragment
        if fragment:
            frag_log = f'{url}#{fragment} in {path}'
            if not isinstance(node, ViewHtml):
                # On none HTML document, not implemented
                log.debug(f'NotImplemented to check fragment {frag_log}')
                return False
            elif not node.check_fragment(fragment):
                log.warning(f'Broken internal link fragment {frag_log}')
                return True

        return False

    @functools.cache
    def check_fragment(self, fragment):
        """Check that this Html contents' has an element with id="`fragment`"

        :param str fragment: The fragment part from an url that must exist
        :rtype: bool
        """
        return contains_id(self.value, fragment)
