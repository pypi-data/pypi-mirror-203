from pathlib import Path

from anytree import Node


class File(bytes):
    """File in a FileSystem, subclasses `bytes`

    :type path: `pathlib.Path`
    :ivar path: the file's path
    """
    def __new__(cls, value):
        self = super().__new__(cls, value.read_bytes())
        return self

    def __init__(self, path):
        self.path = path


class FileSystemImporter(object):
    """Import Tree from FileSystem"""
    def __init__(self, nodecls=Node):
        self.nodecls = nodecls

    def import_(self, directory):
        """Import tree from `directory`."""
        return self.__import(Path(directory))

    def __import(self, path, parent=None):
        node = self.nodecls(path.name, parent=parent)
        if path.is_dir():
            for child in path.iterdir():
                self.__import(child, parent=node)
        elif path.is_file():
            node.value = File(path)
        return node
