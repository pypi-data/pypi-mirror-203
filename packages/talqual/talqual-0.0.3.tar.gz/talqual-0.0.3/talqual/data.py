import json
from operator import attrgetter
from pathlib import Path

import yaml
from anytree import Node, resolver
from anytree.exporter import DictExporter
from docutils.core import publish_doctree


class Data(Node):
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
        """Return the correct Data class for `node`"""
        subtypes = [Yaml, Json, Rst]
        for subtype in subtypes:
            if subtype.match(node):
                return subtype
        return cls

    @classmethod
    def data_from_tree(cls, node):
        subclass = cls.subclass_from_node(node)
        root = subclass(**cls._dict_exporter(node))
        for child in node.children:
            cls.data_from_tree(child).parent = root
        return root

    # unpacking
    def keys(self):
        return map(attrgetter('name'), self.children)

    def __getitem__(self, key):
        r = resolver.Resolver('name')
        return r.get(self, key)


class DataFile(Data):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = Path(self.name).stem
        self._dict_loaded = self.dict_load()

    @classmethod
    def match(cls, node):
        ext = Path(node.name).suffix
        return ext in cls.ext

    # unpacking
    def keys(self):
        return self._dict_loaded.keys()

    def __getitem__(self, key):
        return self._dict_loaded[key]

    def __setitem__(self, key, value):
        self._dict_loaded[key] = value

    def __delitem__(self, key):
        del self._dict_loaded[key]


class Yaml(DataFile):
    ext = ('.yaml', '.yml')

    def dict_load(self):
        return yaml.safe_load(self.value)


class Json(DataFile):
    ext = ('.json', '.jsn')

    def dict_load(self):
        return json.loads(self.value)


class Rst(DataFile):
    ext = ('.rest', '.rst')

    def dict_load(self):
        return self._rst2dict(self.value)

    def _rst2dict(self, text):
        tree = publish_doctree(text).asdom()
        fields = tree.getElementsByTagName('field')

        def parse_field(field):
            name = field.getElementsByTagName('field_name')[0]
            body = field.getElementsByTagName('field_body')[0]

            key = name.firstChild.nodeValue
            value = ' '.join(map(attrgetter('firstChild.nodeValue'),
                                 body.childNodes))

            return (key, value)

        return dict(map(parse_field, fields))
