from typing import List
from collections import deque

n, m = map(int, input().split())

graph:List[List[int]] = [[] for _ in range(n+1)]

for _ in range(m):
    x,y = map(int, input().split())
    graph[y].append(x)

######################################################

maxV = -1e9
answer:List[int] = []

for i in range(1, n+1):
    q = deque()
    q.append((i)) # start, cnt
    visited:List[bool] = [False]*(n+1)
    visited[i] = True
    cnt = 1

    while q:
        node = q.popleft()
        for next_n in graph[node]:
            if not visited[next_n]:
                visited[next_n] = True
                q.append((next_n))
                cnt+=1
    
    if maxV < cnt:
        maxV = cnt
        answer = [i]
    elif maxV == cnt:
        answer.append(i)

answer.sort()
for v in answer:print(v, end=" ")
