from store_vertices import store_vertices
from dijkstra_algo import dijkstra


def main():
    nodes = set()
    graph = dict()
    result = []
    visited = {}
    e = int(input('Enter the number of roads: '))
    store_vertices(e, nodes, graph)
    starting = input('Starting point: ')
    ending = input('ending point point: ')
    unvisited = {node: None for node in nodes}
    current = starting
    current_distance = 0
    unvisited[current] = current_distance
    prev = dijkstra(graph, unvisited, visited, current_distance, current)
    while ending in prev:
        result.append(ending)
        ending = prev[ending]
    result.append(starting)
    print('Shortest path will be: ')
    for i in range(0, len(result)):
        if i < len(result) - 1:
            print(result[len(result) - i - 1], end=' -> ')
        else:
            print(result[len(result) - i - 1])


if __name__ == '__main__':
    main()
