from typing import List
from collections import deque

n,m = map(int, input().split())

graph :List[List[int]]= [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

###################################

def getCavin(num :int) -> int:
    q = deque()
    q.append(num)
    visited :List[int] = [-1 for _ in range(n+1)]
    visited[num] = 0
    while q:
        node = q.popleft()
        for next_n in graph[node]:
            if visited[next_n] == -1:
                visited[next_n] = visited[node]+1
                q.append(next_n)
    result :int = sum(visited) + 1
    return result

min_v = 1e9
answer = None

for i in range(1, n+1):
    cavinValue = getCavin(i)
    if min_v > cavinValue:
        min_v = cavinValue
        answer = i

print(answer)
