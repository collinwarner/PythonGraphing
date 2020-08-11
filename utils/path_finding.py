def shortest_path(graph, n1, n2):
    if n1 not in graph.nodes or n2 not in graph.nodes:
        return "Nodes not in Graph"

    agenda = [[n1]]
    visited = set()



    while agenda:
        temp = []
        for path in agenda:
            tuple_path = tuple(path)
            if tuple_path not in visited:
                visited.add(tuple_path)
                for child in graph.nodes[path[-1]]:
                    if child == n2:
                        res = path.copy()
                        res.append(child)
                        return res
                    t_path = path.copy()
                    t_path.append(child)
                    temp.append(t_path)
        agenda = temp

    return None




