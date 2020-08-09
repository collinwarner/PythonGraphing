from Graph import Graph



if __name__ == "__main__":
    nodes = [1, 2, 3, 4]
    edges = [(1, 2), (2, 3), (3, 4), (4, 2)]
    isDirected = False
    g = Graph(nodes, edges, isDirected)
    print(g)