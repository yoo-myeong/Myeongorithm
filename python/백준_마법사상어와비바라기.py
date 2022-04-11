# 처음구름 세팅 후 반복시작 -> 모든구름을 이동(경계무한) -> 구름칸의 바구니에 물 1 추가 -> 구름칸 하나씩 봐서 그것의 4방향대각선에 물이 있으면 또 1증가-(경계한정) -> 구름칸이 아닌 칸을 확인해서 2이상인 곳만 새로운 구름칸으로 갱신

# 기능 : 구름이동 그래프반환, 4directionCheck, newCloud
from copy import deepcopy

def move(cloud_graph,di,si):
    new_cloud_graph = [[0]*n for _ in range(n)]
    dx, dy = [None, 0, -1, -1, -1, 0, 1, 1, 1], [None, -1, -1, 0, 1, 1, 1, 0, -1]
    for x in range(n):
        for y in range(n):
            if cloud_graph[x][y] == 1:
                nx, ny = (x + dx[di]*si)%n, (y + dy[di]*si)%n
                new_cloud_graph[nx][ny] = 1
    return new_cloud_graph

def fourDirAddWater(cloud_list):
    new_graph = deepcopy(graph)
    dx,dy = [-1,1,1,-1],[-1,-1,1,1]
    for x,y in cloud_list:
        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]
            if 0<=nx<n and 0<=ny<n:
                if graph[nx][ny] >=1:
                    new_graph[x][y]+=1
    return new_graph

def new_cloud(cloud_graph):
    new_cloud_graph = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if cloud_graph[i][j] == 0 :
                if graph[i][j] >=2:
                    new_cloud_graph[i][j] = 1
                    graph[i][j] -=2
    return new_cloud_graph


n,m= map(int, input().split())
cloud_graph = [[0]*n for _ in range(n)]
cloud_graph[n-1][0],cloud_graph[n-1][1],cloud_graph[n-2][0],cloud_graph[n-2][1] = 1,1,1,1
graph = [list(map(int, input().split())) for _ in range(n)]
move_cmd_list = [list(map(int, input().split())) for _ in range(m)]

for di,si in move_cmd_list:
    cloud_graph = move(cloud_graph,di,si)
    cloud_list = []
    for i in range(n):
        for j in range(n):
            if cloud_graph[i][j] == 1:
                cloud_list.append((i,j))
                graph[i][j]+=1 # 구름있는 곳에 1씩 물 추가
    graph = fourDirAddWater(cloud_list)
    cloud_graph = new_cloud(cloud_graph)

answer = 0
for i in range(n):
    for j in range(n):
        answer+=graph[i][j]

print(answer)
