def dfs(graph, source) :
    print(source)
    for element in graph[source]:
        dfs(graph, element)

graph = {
    'A': ['C', 'B'],
    'B': ['D'],
    'C': ['E'],
    'D': ['F'],
    'E': [],
    'F': []
}


dfs(graph, 'A')