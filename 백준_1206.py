from collections import deque
from typing import List, Tuple
n,m,v = map(int, input().split())

graph = [[] for _ in range(n+1)]
for i in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for elements in graph:elements.sort()

def bfs():
    answer = [v]
    visited = [False]*(len(graph)+1)
    q = deque()
    q.append(v)
    visited[v] = True
    while q:
        node = q.popleft()
        elements:List[int] = graph[node]
        for e in elements:
            if not visited[e]:
                answer.append(e)
                visited[e] = True
                q.append(e)
    return answer

def dfs():
    answer = [v]
    visited = [False]*(len(graph)+1)
    visited[v] = True
    def recurse(node):
        elements:List[int] = graph[node]
        for e in elements:
            if not visited[e]:
                visited[e] = True
                answer.append(e)
                recurse(e)
    recurse(v)
    return answer

dfs_result = dfs()
for x in dfs_result: print(x, end=" ")
print()
bfs_result = bfs()
for x in bfs_result: print(x, end=" ")
