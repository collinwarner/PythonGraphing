from Graph import Graph
from Visualize import convert_graph_to_plot


if __name__ == "__main__":
    nodes = [1, 2, 3, 4]
    edges = [(1, 2), (2, 3), (3, 4), (4, 2)]
    isDirected = False
    g = Graph(nodes, edges, isDirected)
    convert_graph_to_plot(g)
    print(g)