def dfs(graph,v,visited):
  visited[v] = True
  print(v,end=' ')
  for i in graph[v]:
    if not visited[i]:
      dfs(graph,i,visited)

graph= [
[],
[2,3,8],
[1,7],
[1,4,5],
[3,5],
[3,4],
[7],
[2,6,8],
[1,7]
]

def dfs_stack(graph, start_node):
  visit = list()
  stack = list()
  stack.append(start_node)

  while stack:
      node.append(node)
      stack.extend(graph[node])
  return visit

visited =[False] *9

dfs(graph,1,visited)
