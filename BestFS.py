import heapq

def best_first_search(graph, heuristic, start, goal):
    open_list = []
    closed = set()
    heapq.heappush(open_list, (heuristic[start], start))

    while open_list:
        _, current = heapq.heappop(open_list)
        if current in closed:
            continue
        closed.add(current)

        print("Visiting:", current)
        if current == goal:
            print("Goal found!")
            return True
        for neighbour in graph[current]:

            if neighbour not in closed:
                heapq.heappush(
                    open_list,
                    (heuristic[neighbour], neighbour)
                )

    print("Goal not found!")
    return False

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}
heuristic = {
    'A': 6,
    'B': 4,
    'C': 2,
    'D': 7,
    'E': 5,
    'F': 3,
    'G': 0
}


best_first_search(graph, heuristic, 'A', 'G')