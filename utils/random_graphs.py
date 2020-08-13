import random
from Graph import Graph
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors
from matplotlib.ticker import PercentFormatter

def create_uniform_graph(n, connection_probability):
    edges = []
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i !=j:
                if random.random() < connection_probability:
                    edges.append((i,j))
    print("found_edges")
    return Graph(n, edges, False)

def get_degreeSequence(graph):
    return [len(graph.nodes[node]) for node in graph.nodes]

def get_expected_degree(degree_sequence):
    return sum(degree_sequence)/len(degree_sequence)

def get_probability_d_n(d_n, k):
    res = 0
    for d_i in d_n:
        if d_i == k:
            res+=1
    return res/len(d_n)

def joint_law_x_n_y_n(graph):

    def inside(k, l):
        res = 0
        for edge in graph.edges:
            if edge[0] == k and edge[1] == l:
                res += 1/len(graph.nodes[edge[0]])
        return res/len(graph.nodes)

    return inside

def friends_have_more_friends(graph):
    p = joint_law_x_n_y_n(graph)
    E_x_n = sum()
def friends_in_random_friendship(graph, k):
    d_n = get_degreeSequence(graph)
    E_D_n = get_expected_degree(d_n)
    P_D_n = get_probability_d_n(d_n, k)
    return k/E_D_n*P_D_n

def graph_histogram(graph):
    plt.clf()
    degree_sequence = get_degreeSequence(graph)
    n = len(graph.nodes)
    bins = [i for i in range(n)]

    plt.hist(degree_sequence, bins=bins)
    plt.show()


