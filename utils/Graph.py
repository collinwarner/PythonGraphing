class Graph:

    def __init__(self, nodes, edges, isDirected):
        self.nodes = {}
        self.edges = set()
        self.isDirected = isDirected
        self.initialize_graph(nodes, edges)
    
    #initialize graph from list of numbers for nodes, and list of tuples for connections
    #O(n+e) time and O(n+e) space
    def initialize_graph(self, nodes, edges):       
        for edge in edges:
            self.addEdge(edge)
            
        for node in range(1, nodes+1):
            self.addNode(node)

            

    def addEdge(self, edge):
        n1, n2 = edge
        if not self.isDirected:
            self.nodes[n2] = self.nodes.setdefault(n2, set()) | {n1}
            self.edges.add((n2, n1))
        self.nodes[n1] = self.nodes.setdefault(n1, set()) | {n2}
        self.edges.add((n1, n2))
    
    def addNode(self, n):
        if n not in self.nodes:
            self.nodes[n] = set()
    
    def remove_node(self, node):
        if node in self.nodes:
            for otherNode in self.nodes[node]:
                if not self.isDirected:
                    self.edges.remove((otherNode, node))
                    self.nodes[otherNode].remove(node)
                self.edges.remove((node, otherNode))
            self.nodes.pop(node)

    def remove_edge(self, edge):
        if edge in self.edges:
            if not self.isDirected:
                self.edges.remove((edge[1], edge[0]))
                self.nodes[edge[1]].remove(edge[0])
            self.edges.remove(edge)
            self.nodes[edge[0]].remove(edge[1])

            
    def __repr__(self):
        return f"{list(self.nodes.keys())} / {list(self.edges)} / {self.isDirected}"

        
    def __str__(self):
        res = ""
        for node in self.nodes:
            res += f"Node {node} is connected to Nodes {self.nodes[node]} \n"
        
        res += f"Edges are {self.edges}"

        return res


def convert_back(in_graph):
    if in_graph:
        nodes, edges, is_directed = in_graph.split("/")
        print(is_directed)
        nodes,edges = tokenizer(nodes), tokenizer(edges)
        nodes = list(map(int, nodes.split()))
        edges = list(map(int, edges.split()))
        edges = [(edges[i - 1], edges[i]) for i in range(1, len(edges), 2)]
        is_directed = True if is_directed.strip() == "True" else False
        g = Graph(len(nodes), edges, is_directed)
        print(g)
        return g
    return None
def tokenizer(_input):
    _input = _input.replace("[", "")
    _input = _input.replace("]", "")
    _input = _input.replace(",", "")
    _input = _input.replace("(", "")
    _input = _input.replace(")","")
    return _input
