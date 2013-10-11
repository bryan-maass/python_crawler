from crawler.ProjectCrawler import Crawler
import os
from pprint import pprint
from functools import partial
from pprint import pprint as p
from graph.Edge import Edge, DirectedEdge
from graph.graph_plot_panel import GraphPlotPanel

crawler = Crawler()

graph = GraphPlotPanel(edge_class=DirectedEdge)

graph.graphviz("/Users/bcm/PycharmProjects/python_crawler/graph.dot")
graph.run()