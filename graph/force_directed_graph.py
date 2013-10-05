from graph_plot_panel import GraphPlotPanel


def launch_graph_plot():
    gp = GraphPlotPanel()
    # graph_plot.buildRandomGraph(number_of_vertices, edge_rate)


    for x in range(gp.number_of_vertices):
        gp.add_vertex()
    for y in range(gp.number_of_edges):
        gp.add_edge()
    gp.run()

if __name__ == "__main__":
    launch_graph_plot()


