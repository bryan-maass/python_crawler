import os
import pygraphviz


class ProjectCrawler():
    """makes a directory tree into a python dictionary"""
    def __init__(self, root):
        pass


class Directory():
    def __init__(self, name, full_path, files=None, dirs=None):
        self.name = name
        self.full_path = full_path
        self.files = files
        self.dirs = dirs

