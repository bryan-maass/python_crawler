import os
import pygraphviz


class Crawler():
    """makes a directory tree into a python dictionary"""
    def __init__(self):
        pass

    def target(self, path):
        """
        returns the node, its children, its parents, and its siblings
        """
        parent = os.path.dirname(path)
        siblings = self.fill(parent)
        children = self.fill(path)

        return parent, siblings, children

        #parent[path] = children

    def fill(self, path):
        try:
            contents = os.listdir(path)
        except:
            return
        files = [f for f in contents if os.path.isfile(os.path.join(path, f))]
        dirpaths = [os.path.join(path, d) for d in contents if os.path.isdir(os.path.join(path, d))]
        return (dirpaths, files)


class Node():
    def __init__(self, full_path, files=None, dirs=None):
        self.parent, self.name = os.path.split(full_path)
        self.isdir = os.path.isdir(full_path)
        self.full_path = full_path
        self.files = self.isdir and files
        self.dirs = self.isdir and dirs


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
        returns a graphviz graph as a string
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





