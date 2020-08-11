from Graph import Graph
from Visualize import convert_graph_to_plot, save_fig
from path_finding import shortest_path

from random_graphs import create_uniform_graph
if __name__ == "__main__":
    nodes = [1, 2, 3, 4, 5]
    edges = [(1, 5), (5,2), (2,3), (3,4), (2,4), (1, 4)]
    isDirected = False
    g = create_uniform_graph(10, 0.2)
    save_fig(g, "test1.png")
    sp = shortest_path(g, 1, 4)
    print("shortest path from 1->3: " ,sp)


    print(g)