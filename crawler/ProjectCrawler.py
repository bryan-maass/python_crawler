import os
import pygraphviz


class ProjectCrawler():
    """makes a directory tree into a python dictionary"""
    def __init__(self, root):
        pass


class Node():
    def __init__(self, full_path, files=None, dirs=None):
        self.parent, self.name = os.path.split(full_path)
        self.isdir = os.path.isdir(full_path)
        self.full_path = full_path
        self.files = self.isdir and files
        self.dirs = self.isdir and dirs
        self.scan_dir()

    def scan_dir(self):
        contents = os.listdir(self.full_path)
        files = [f for f in contents if os.path.isfile(os.path.join(self.full_path, f))]
        self.files = files
        dirpaths = [os.path.join(self.full_path, d) for d in contents if os.path.isdir(os.path.join(self.full_path, d))]
        dirpaths = filter(lambda x: ".git" not in x, dirpaths)
        self.dirs = [Node(d) for d in dirpaths]

    def __str__(self):
        s = "\n" + "------" + "\n"
        s += self.full_path + "\n"
        for f in self.files:
            s += "f:\t" + str(f) + "\n"
        for d in self.dirs:
            s += "d:\t" + str(d) + "\n"
        return s

    def to_graphviz(self):
        """
        @rType: String
        returns a graphviz graph string
        """
        s = "digraph G {\n"
        s += " main [shape=box]; "
        s += self.gv_data()
        s += "}"
        return s

    def gv_data(self):
        me = self.full_path
        s = ""
        for f in self.files:
            s += "\"" + me + "\"" + " -> " + "\"" + f + "\"" + ";\n"
        for d in self.dirs:
            s += "\"" + me + "\"" + " -> " + "\"" + d.full_path + "\"" + ";\n"
            s += d.gv_data()
        return s


