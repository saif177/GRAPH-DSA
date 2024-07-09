def dfs(graph, source) :
  stack = [source]
  while stack :
      curr = stack.pop()
      print(curr)
       
      for elmnt in graph[curr] :
          stack.append(elmnt)


graph = {
    'A': ['C', 'B'],
    'B': ['D'],
    'C': ['E'],
    'D': ['F'],
    'E': [],
    'F': []
}


dfs(graph, 'A')