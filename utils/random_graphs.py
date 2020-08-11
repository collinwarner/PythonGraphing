import random
from Graph import Graph

def create_uniform_graph(n, connection_probability):
    nodes = [i for i in range(1, n+1)]
    edges = []
    for i in nodes:
        for j in nodes:
            if i !=j:
                if random.random() < connection_probability:
                    edges.append((i,j))
    return Graph(nodes, edges, False)

