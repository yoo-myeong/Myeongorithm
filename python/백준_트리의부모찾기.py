from typing import List, Tuple, Dict
from collections import deque

n :int = int(input())
graph :Dict[int, List[int]] = {}
for i in range(1,n+1) : graph[i] = []

for _ in range(n-1):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

##############

arr :List[int] = [None for _ in range(n+1)]
arr[1] = 0
q = deque()

for node in graph[1]:
    arr[node] = 1
    q.append(node)

while q:
    node :int = q.popleft()
    next_nodes :List[int] = graph[node]

    for next_node in next_nodes:
        if arr[next_node] == None:
            arr[next_node] = node
            q.append(next_node)

for i in range(2,len(arr)):
    print(arr[i])
