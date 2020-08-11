import matplotlib.pyplot as plt
import random
import math


def convert_graph_to_plot(graph):
    plt.clf()
    n = len(graph.nodes)
    node_coords = {}


    gen = (node for node in graph.nodes)
    nroot = int(math.sqrt(n))+1
    for x in range(1, nroot+1):
        try:
            for y in range(1, nroot):
                node = next(gen)
                node_coords[node] = (x, y)
                plt.plot(x, y, 'ro', color='black', markersize=20)
                plt.text(x, y, node, color='white')
        except StopIteration:
            break



    for edge in graph.edges:
        n1x, n1y = node_coords[edge[0]]
        n2x, n2y = node_coords[edge[1]]
        plt.plot([n1x, n2x], [n1y, n2y], "k")
    plt.tick_params(
        axis='x',  # changes apply to the x-axis
        which='both',  # both major and minor ticks are affected
        bottom=False,  # ticks along the bottom edge are off
        top=False,  # ticks along the top edge are off
        labelbottom=False)  # labels along the bottom edge are off
    plt.tick_params(
        axis='y',  # changes apply to the x-axis
        which='both',  # both major and minor ticks are affected
        left=False,  # ticks along the bottom edge are off
        right=False,  # ticks along the top edge are off
        labelleft=False
    )
    plt.xlim(0, nroot+1)
    plt.ylim(0, nroot+1)


def save_fig(g, filename):
    convert_graph_to_plot(g)
    plt.savefig("../flaskr/static/graph_plots/"+filename)

if __name__=="__main__":
    convert_graph_to_plot(1)