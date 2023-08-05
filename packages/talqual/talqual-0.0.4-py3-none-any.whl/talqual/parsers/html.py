import re
from functools import partial
from html.parser import HTMLParser
from urllib.parse import urlparse


class LinksParser(HTMLParser):
    """Parser for extracting all href attributes from an HTML document

    :ivar parsed_href: The values for href
    :type parsed_href: list of str
    """

    def __init__(self):
        super().__init__()
        self.parsed_hrefs = set()
        self.base_href = None

    def _handle_attrs(self, attrs):
        """
        :param attrs: [('href', 'index.html'),]
        :type attrs: list of tuple
        :returns: The value for href or None for not found
        :rtype: str or None
        """
        for attr, value in attrs:
            if attr in ('href', 'src'):
                return value

    def handle_starttag(self, tag, attrs):
        href = self._handle_attrs(attrs)
        if tag.lower() == 'base':
            # BASE HREF
            if not href.endswith('/'):
                href += '/'
            self.base_href = href
        elif href is not None:
            self.parsed_hrefs.add(href)


def get_link_info(link, base_href=None):
    """
    Parses the `link` with `base_href`,
    separating the #`fragment` part and ignoring the ?query part.

    Classifies the url as external or internal.

    :type str link: An internal or external url
    :type str base_href: The attribute href for HTML base element
    :rtype: tuple('external'|'internal, base+link, fragment)
    """
    url = urlparse(link)
    url_base = urlparse(base_href)
    fragment = None
    dst = 'external'

    if not url.netloc and not url_base.netloc:
        # internal only when internal links and base_href is also internal
        dst = 'internal'
        link = url.path
        fragment = url.fragment

    if base_href and not url.netloc:
        # Insert base_href only to internal links
        link = base_href + link

    return (dst, link, fragment)


def get_all_href(html):
    """
    :type html: str
    :rtype: list of tuple(:py:func:`get_link_info`)
    """
    links_parser = LinksParser()
    links_parser.feed(html)
    links_parser.close()

    partial_info = partial(get_link_info, base_href=links_parser.base_href)
    return map(partial_info, links_parser.parsed_hrefs)


def contains_id(html, id_):
    """`html` document contains an element with attribute id="`id_`"?

    :param str html: The HTML document
    :param str id_: The id="`id_`" to search
    :rtype: boolean
    """
    pattern = f'id=\"{id_}\"|id=\'{id_}\''
    return bool(re.search(pattern, html))
