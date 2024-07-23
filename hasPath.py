visited = set()
def hasPath(graph, src, dst) :
    if src == dst : return True
    for curr in graph[src] :
        if curr not in visited:
            visited.add(curr)
            if(hasPath(graph, curr, dst) == True):
                return True
            else :
                return False
    return False

graph = {
    'f': ['g', 'i'],
    'g': ['h'],
    'h': [],
    'i': ['g', 'k'],
    'j': ['i'],
    'k': []
}

start = 'f'
destination = 'k'
print(hasPath(graph, start, destination))