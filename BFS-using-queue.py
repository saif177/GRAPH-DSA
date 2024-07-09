from collections import deque

def bfs(graph, source) :
    queue = deque([source])

    while queue :
        current = queue.pop()
        print(current)

        for element in graph[current] :
            queue.appendleft(element)             

graph = {
    'A': ['C', 'B'],
    'B': ['D'],
    'C': ['E'],
    'D': ['F'],
    'E': [],
    'F': []
}


bfs(graph, 'A')