import os
import pygraphviz


class ProjectCrawler():
    """makes a directory tree"""

    def __init__(self, root):
        self.root = root

    def scan(self):
        for dirname, dirnames, filenames in os.walk(self.root):
            # print path to all subdirectories first.
            for subdirname in dirnames:
                print os.path.join(dirname, subdirname)

            # print path to all filenames.
            for filename in filenames:
                print os.path.join(dirname, filename)

            # Advanced usage:
            # editing the 'dirnames' list will stop os.walk() from recursing into there.
            if '.git' in dirnames:
                # don't go into any .git directories.
                dirnames.remove('.git')
