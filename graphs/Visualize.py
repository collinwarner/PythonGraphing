import matplotlib.pyplot as plt
import random

def convert_graph_to_plot(graph):
    n = 3*len(graph.nodes)
    node_coords = {}
    for node in graph.nodes:
        x, y = (int(random.random()*n), int(random.random()*n))
        print("x", x)
        print("y", y)
        node_coords[node] = (x, y)
        plt.plot(x, y,'ro',  color='black', markersize=20)
        plt.text(x, y, node, color='white')

    for edge in graph.edges:
        n1x, n1y = node_coords[edge[0]]
        n2x, n2y = node_coords[edge[1]]
        plt.plot([n1x, n2x], [n1y, n2y], "k")
    plt.xlim(-1, n+1)
    plt.ylim(-1, n+1)
    plt.show()

if __name__=="__main__":
    convert_graph_to_plot(1)