# 조합 찾아서 최소시간 구하기
from itertools import combinations
from collections import deque
from copy import deepcopy

n,m = map(int, input().split())
zero_cnt = 0

graph, virus_point = [], []
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] == 2 : virus_point.append((i,j))
        if graph[i][j] == 0 : zero_cnt+=1

def bfs(g,viruses):
    graph = deepcopy(g)
    q = deque()
    q2 = deque()
    for x,y in viruses:
        graph[x][y] = 3
        q.append((x,y,0))
    zero = 0
    last_cnt = None
    while q:
        x,y,cnt = q.popleft()
        last_cnt = cnt
        for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx,ny = x+dx, y+dy
            if 0<=nx<n and 0<=ny<n:
                if graph[nx][ny] == 0 or graph[nx][ny] == 2:
                    if graph[nx][ny] == 0: zero += 1
                    if zero == zero_cnt: return last_cnt + 1
                    graph[nx][ny] = 3
                    q.append((nx,ny,cnt+1))
    if zero == zero_cnt : return last_cnt
    else : return "False"

viruses_combi = combinations(virus_point,m)
answer = 1e9
for viruses in viruses_combi:
    if zero_cnt==0 :
        answer = 0
        break
    result = bfs(graph, viruses)
    if result != "False":
        answer = min(answer, result)

if answer == 1e9 : print(-1)
else : print(answer)
