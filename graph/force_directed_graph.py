from graph_plot_panel import GraphPlotPanel
from time import sleep
from Edge import DirectedEdge
def launch_graph_plot():
    gp = GraphPlotPanel()
    gp.pretty_graph()


g = GraphPlotPanel(edge_class=DirectedEdge)
g.run()
