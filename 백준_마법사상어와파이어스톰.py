from collections import deque
from copy import deepcopy
# 어떤 그래프를 넣든 시계방향 90도 회전한 그래프로 반환
def rotate(graph):
    new_graph = [[0]*len(graph[0]) for _ in range(len(graph))]
    for i in range(len(graph)):
        for j in range(len(graph)):
            new_graph[j][len(graph)-i-1] = graph[i][j]
    return new_graph
# 새그래프와 좌표를 넣으면 좌표를 시작점으로 그래프에 갱신
def updategraph(new_graph,x,y):
    for i in range(len(new_graph)):
        for j in range(len(new_graph)):
            graph[i+x][j+y] = new_graph[i][j]
# 좌표를 대입하면 얼음이있는 인접칸의 개수를 반환
def Check4dir(x,y,copy_graph):
    dx,dy = [-1,1,0,0],[0,0,1,-1]
    cnt = 0
    for i in range(4):
        nx,ny = x+dx[i],y+dy[i]
        if 0<=nx<len(copy_graph) and 0<=ny<len(copy_graph):
            if copy_graph[nx][ny]>=1: cnt+=1
    return cnt

n,q = map(int, input().split())
n = 2**n
graph = [list(map(int, input().split())) for _ in range(n)]
cmd_list = list(map(int, input().split()))

for l in cmd_list:
    l = 2**l
    for i in range(0,n,l):
        for j in range(0,n,l):
            new_graph = []
            for k in range(i,i+l):
                new_graph.append(graph[k][j:j+l])
            new_graph = rotate(new_graph)
            updategraph(new_graph,i,j)
    copy_graph = deepcopy(graph)
    for i in range(n):
        for j in range(n):
            if Check4dir(i,j,copy_graph) < 3:
                if graph[i][j]>0:graph[i][j]-=1

sum_val, max_group  = 0, -1e9
for i in range(n):
    for j in range(n):
        sum_val += graph[i][j]

visited = [[False]*n for _ in range(n)]
dx,dy = [-1,1,0,0],[0,0,1,-1]
for i in range(n):
    for j in range(n):
        if visited[i][j] == False and graph[i][j]!=0:
            visited[i][j] = True
            q = deque()
            q.append((i,j))
            group_cnt = 1
            while q:
                x,y = q.popleft()
                for d in range(4):
                    nx,ny = x+dx[d], y+dy[d]
                    if 0<=nx<n and 0<=ny<n:
                        if visited[nx][ny] == False and graph[nx][ny]!=0:
                            visited[nx][ny] = True
                            group_cnt+=1
                            q.append((nx,ny))
            max_group = max(group_cnt,max_group)

print(sum_val)
if max_group <= 1 : print(0)
else: print(max_group)
