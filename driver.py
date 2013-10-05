from crawler.ProjectCrawler import ProjectCrawler, Directory
import os
from functools import partial
from pprint import pprint as p

def fill(root_path):
    dict = {}
    tree = {}
    full_paths = os.listdir(root)
    dirs = [d for d in os.listdir(root) if os.path.isdir(os.path.join(root, d))]
    files = [f for f in os.listdir(root) if os.path.isfile(os.path.join(root, f))]
    d = Directory
    dict['name'] = os.path.split(root_path)[-1]
    dict['full_path'] = root_path
    dict['files'] = files
    dict['dirs'] = dirs
    return dict

def children(root_path):

root = "/Users/bcm/dev/clojure-koans"

p(fill(root))