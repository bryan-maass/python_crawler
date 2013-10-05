from crawler.ProjectCrawler import ProjectCrawler, Node
import os
from functools import partial
from pprint import pprint as p


my_dir = "/Users/bcm/dev/clojure-koans"

d = Node(my_dir)

if os.path.isfile("graph.dot"):
    os.remove("graph.dot")

with open("graph.dot", "w") as f:
    f.write(d.to_graphviz())

#print d