def shortest_path(graph, n1, n2):
    if n1 not in graph.nodes or n2 not in graph.nodes:
        return "Nodes not in Graph"

    agenda = [(n1,)]
    visited = set()

    while agenda:
        temp = []
        for path in agenda:
            if path[-1] not in visited:
                visited.add(path[-1])
                for child in graph.nodes[path[-1]]:
                    if child == n2:
                        return path + (child, )
                    temp.append(path + (child, ))
        agenda = temp

    return None
