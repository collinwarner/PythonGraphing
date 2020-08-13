from Graph import Graph
from Visualize import convert_graph_to_plot, save_fig
from path_finding import shortest_path
import random
from random_graphs import *

import time
if __name__ == "__main__":
    nodes = 5
    edges = [(1, 5), (5,2), (2,3), (3,4), (2,4), (1, 4)]
    isDirected = False
    start = time.time()
    n = 10
    g = create_uniform_graph(n, 0.3)
    end = time.time()
    print("time to create graph", end-start)


    save_fig(g, "test1.png")
    """

    for i in range(1000):
        a, b = random.randint(1, n), random.randint(1, n)
        if a == b:
            b += 1
        start = time.time()
        sp = shortest_path(g, a, b)
        end = time.time()
        print("time to find path", round(end-start, 4))
        print(f"length of shortest path from {a}->{b} is {len(sp) if sp is not None else None} ")

    p_x_y = joint_law_x_n_y_n(g)
    print(p_x_y(1, 2))

    #print(g)
    #graph_histogram(g)
    #print(friends_in_random_friendship(g, 2))
    """