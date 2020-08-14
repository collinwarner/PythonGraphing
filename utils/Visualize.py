import matplotlib.pyplot as plt
import random
import math
import numpy as np

def convert_graph_to_plot(graph, path):
    #O(n)
    print(path)
    path_convert = set()
    if path:
        path_convert = set([(path[i-1], path[i]) for i in range(1, len(path))])

    plt.clf()
    n = len(graph.nodes)+1
    arc_seperation = 1
    rads_per_node = 2*np.pi/n
    r = 1/rads_per_node
    node_coords = {}
    theta = 0
    for node in graph.nodes:
        x, y = r*np.cos(theta), r*np.sin(theta)
        theta += rads_per_node
        node_coords[node] = (x, y)
        plt.plot(x, y, 'ro', color='black', markersize=20)
        plt.text(x, y, node, color='white')





    for edge in graph.edges:
        n1x, n1y = node_coords[edge[0]]
        n2x, n2y = node_coords[edge[1]]
        if edge in path_convert or (edge[1], edge[0]) in path_convert:
            plt.plot([n1x, n2x], [n1y, n2y], "red")
            if graph.isDirected:
                dx, dy = (n2x - n1x)/2, (n2y - n1y)/2
                plt.arrow(n1x, n1y, dx, dy, head_width=0.1, color="red")
        else:
            if graph.isDirected:
                dx, dy = (n2x - n1x) / 2, (n2y - n1y) / 2
                plt.arrow(n1x, n1y, dx, dy, head_width=0.1, color="k")
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

    plt.xlim(-r-1, r+1)
    plt.ylim(-r-1, r+1)


def save_fig(g, filename, path = []):
    convert_graph_to_plot(g, path)
    plt.savefig("../flaskr/static/graph_plots/"+filename)

if __name__=="__main__":
    convert_graph_to_plot(1)