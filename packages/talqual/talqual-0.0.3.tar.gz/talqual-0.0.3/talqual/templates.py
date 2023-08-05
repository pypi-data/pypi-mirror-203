from importlib import resources
from pathlib import Path

from anytree import Node
from anytree.exporter import DictExporter
from anytree.resolver import Resolver

from .batch import Batch
from .translation import Translation
from .views import CollectionView, View, ViewHtml
from .zpt import PageTemplate


class Template(Node):
    """
    def __init__(self, name, parent=None, children=None, **kwargs):
    self.__dict__.update(kwargs)

    * self.value: File contents
    """

    def _dict_exporter(self):
        """Export to dict without children neither parent"""
        exporter = DictExporter(maxlevel=0)
        return exporter.export(self)

    @classmethod
    def subclass_from_node(cls, node):
        """Return the correct Template class for `node`"""
        subtypes = [NoView, TalCommand, Folder, HtmlPt]
        for subtype in subtypes:
            if subtype.match(node):
                return subtype
        return cls

    @classmethod
    def template_from_tree(cls, node):
        subclass = cls.subclass_from_node(node)

        root = subclass(**cls._dict_exporter(node))
        for child in node.children:
            cls.template_from_tree(child).parent = root
        return root

    def load_template(self, path, context=None):
        """Loader implementation for zpt loading macros

        :param str path: The path to a macro from inside a template
        :param context: The template where loading
        :type context: :class:`.zpt.PageTemplate`
        :rtype: :class:`.zpt.PageTemplate`
        """
        template = Resolver('name').get(self, path.strip())
        return PageTemplate(template.value,
                            extra_builtins=context.extra_builtins)

    def render(self, data):
        if self.is_root and isinstance(self, Folder):
            # first time
            PageTemplate.loader_search = self.load_template

        return View(**self._dict_exporter())

    @property
    def locales(self):
        try:
            return self._locales
        except AttributeError:
            return Translation()

    def set_locales(self, locales):
        self._locales = locales

    def full_path(self):
        """Return the full path from root to this node

        :rtype: str
        """
        sep = self.separator
        return sep.join([""] + [str(node.name) for node in self.path])

    def relative_path(self):
        """Return the relative path from root to this node

        :rtype: str
        """
        path = self.full_path()
        while path.startswith('/'):
            path = path[1:]
        return path


class HtmlPt(Template):
    """
    * self._template
    """
    ext = ('.html', '.htm', '.pt')

    @classmethod
    def match(cls, node):
        ext = Path(node.name).suffix
        return ext in cls.ext

    def chameleon_template(self):
        return PageTemplate(self.value,
                            translate=self.locales.translate,
                            extra_builtins={'url': self.relative_url})

    def relative_url(self, url):
        """Transform the url to relative

        :param str url: The url absolue
        :return: A new url computed relatively
        :rtype: url
        """
        url = url.strip()
        relative_base = len(self.path)-2

        shared_path = 0
        # compute shared path betwen url and self
        path_self = self.relative_path().split('/')
        path_url = url.split('/')
        for a, b in zip(path_self, path_url):
            if a != b:
                break
            shared_path += 1

        if shared_path > 0:
            url = '/'.join(path_url[shared_path:])
            if not url and relative_base == shared_path:
                # special case referencing parent folder
                return './'

        relative_url = '../'*(relative_base-shared_path)
        return relative_url + url

    def render(self, data):
        name = self.name
        if name.endswith('.pt'):
            name = Path(name).with_suffix('.html')

        lang = self.locales.current_language(data)
        value = self.chameleon_template().render(**data, target_language=lang)
        return ViewHtml(name=name, value=value)


class Folder(Template):

    @classmethod
    def match(cls, node):
        return not node.is_leaf

    def render(self, data):
        root = super().render(data)
        for child in self.children:
            view = child.render(data)
            if view:
                if isinstance(view, CollectionView):
                    for v in view.children:
                        v.parent = root
                else:
                    view.parent = root
        return root

    def set_locales(self, locales):
        super().set_locales(locales)
        for child in self.children:
            child.set_locales(locales)


class NoView(Template):
    prefix = '_'

    @classmethod
    def match(cls, node):
        return node.name.startswith(cls.prefix)

    def render(self, data):
        pass


class TalCommand(Template):
    prefix = '.tal_'

#    taldefine = 'tal_define_'

    @classmethod
    def match(cls, node):
        return cls.prefix in node.name

    def get_command(self, stem):
        commands = [TalCommandRepeat, TalCommandBatch, TalCommandReplace]

        for command in commands:
            if command.prefix in stem:
                return command
        return None

    def get_subtype(self):
        """Is a Folder or a HtmlPt?"""
        if Folder.match(self):
            return Folder
        elif HtmlPt.match(self):
            return HtmlPt
        return Template

    def render(self, data):
        """Return `CollectionView` with all rendered subviews"""
        collection = CollectionView(self.name)
        subtype = self.get_subtype()

        name = Path(self.name)
        stems = name.stem.split(self.prefix)
        base_name = stems[0]
        ext = name.suffix
        if ext.startswith(self.prefix):
            # there is no suffix in name
            stems.append(ext[len(self.prefix):])
            ext = ''

        for stem in stems:
            command = self.get_command(stem)
            if command is not None:
                stems.remove(stem)
                template = subtype(**self._dict_exporter(),
                                   children=self.children,
                                   parent=self.parent)  # add virtually
                template.set_locales(self.locales)
                command = command(collection, template, data, base_name, ext)
                parameters = stem[len(command.prefix):]
                command.execute(parameters)
                template.parent = None  # template is virtual

        return collection


class TalCommandType():
    def __init__(self, collection, template, data, base_name, ext):
        self.collection = collection
        self.template = template
        self.data = data
        self.base_name = base_name
        if ext == '.pt':
            ext = '.html'
        self.ext = ext

    def _parse_data_variables(self, parameters):
        """Separated by `:`"""
        variables = parameters.split(':')
        if variables[-1] == '':
            del variables[-1]
        data = self.data
        for var in variables:
            data = data[var]
        return data

    def _replace_data_variables(self, parameters, new_value):
        """Separated by `:`"""
        variables = parameters.split(':')
        data_parent = self._parse_data_variables(':'.join(variables[:-1]))
        data_parent[variables[-1]] = new_value


class TalCommandRepeat(TalCommandType):
    prefix = 'repeat_'

    def _get_name(self, item, num):
        if self.base_name == 'tal_':
            # item.ext
            return f'{item}{self.ext}'
        else:
            # name.num.ext
            return f'{self.base_name}.{num}{self.ext}'

    def execute(self, parameters):
        items = self._parse_data_variables(parameters)
        for num, item in enumerate(items):
            # set repeat info into data
            key = f'tal_{self.prefix}{parameters}'
            info = {'num': num, 'item': item}
            self.data[key] = info

            # temporally set new name to template while rendering
            new_name = self._get_name(item, num)
            self.template.name, original = new_name, self.template.name
            view = self.template.render(self.data)
            self.template.name = original

            # set new name to view
            view.name = new_name
            view.parent = self.collection

            # remove repeat info from data
            del self.data[key]


class TalCommandBatch(TalCommandType):
    prefix = 'batch_'

    def execute(self, parameters):
        variable, size = parameters.split('_')
        size = int(size)
        items = self._parse_data_variables(variable)
        for page in Batch(items, size, base_name=self.base_name + self.ext):
            self._replace_data_variables(variable, page)
            view = self.template.render(self.data)
            view.name = page.url
            view.parent = self.collection
        self._replace_data_variables(variable, items)


class TalCommandReplace(TalCommandType):
    prefix = 'replace_'

    def execute(self, parameters):
        if parameters == 'talqual_scripts':
            pkg = 'talqual.static'
            transcrypt_js = 'org.transcrypt.__runtime__.js'
            value = resources.files(pkg).joinpath('scripts.js').read_bytes()
            template = Template(f'{self.base_name}{self.ext}', value=value)
            view = template.render(self.data)
            view.parent = self.collection
            value2 = resources.files(pkg).joinpath(transcrypt_js).read_bytes()
            template2 = Template(transcrypt_js, value=value2)
            view2 = template2.render(self.data)
            view2.parent = self.collection
            return

        # data replacing
        item = self._parse_data_variables(parameters)
        template = Template(f'{self.base_name}{self.ext}', value=item.value)
        view = template.render(self.data)
        view.parent = self.collection
        return
