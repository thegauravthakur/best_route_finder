def store_vertices(e, nodes, graph):
    for i in range(0, e):
        u, v, d = input('Enter the starting point, ending point and distance for path {}: '.format(i + 1)).split()
        # u, v, d = input().split()
        if u not in nodes:
            graph[u] = {v: int(d)}
            nodes.add(u)
        else:
            temp = graph[u]
            temp[v] = int(d)
        if v not in nodes:
            graph[v] = {u: int(d)}
            nodes.add(v)
        else:
            temp = graph[v]
            temp[u] = int(d)
