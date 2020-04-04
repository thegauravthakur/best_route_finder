def dijkstra(graph, unvisited, visited, current_distance, current):
    prev = dict()
    while True:
        for nbr, distance in graph[current].items():
            if nbr not in unvisited:
                continue
            newDistance = current_distance + distance
            if unvisited[nbr] is None or unvisited[nbr] > newDistance:
                unvisited[nbr] = newDistance
                prev[nbr] = current
        visited[current] = current_distance
        del unvisited[current]
        if not unvisited:
            break
        candidates = [node for node in unvisited.items() if node[1]]
        current, current_distance = sorted(candidates, key=lambda x: x[1])[0]
    return prev
