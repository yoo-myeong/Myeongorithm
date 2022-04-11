# 상어이동함수
# 이동시킬 상어 좌표를 받는다. # 좌표의 그래프에 [속력, 방향, 크기]가 있다
# 방향은 위,아래,우,좌 범위를 넘으면 ((방향+1)//2)를 적용
# 속력만큼 for문 돌려서 이동시켜준다.
from copy import deepcopy
def shark_move(x,y):
    dx, dy = [0,-1,1,0,0], [0,0,0,1,-1]
    s,d,z = graph[x][y]
    nx,ny = x,y
    for _ in range(s):
        nx, ny = nx+dx[d], ny+dy[d]
        if nx<0 or nx>=len(graph) or ny<0 or ny>=len(graph[0]):
            nx, ny = nx - dx[d], ny - dy[d]
            if d == 1 : d = 2
            elif d == 2 : d = 1
            elif d == 3: d = 4
            elif d == 4: d = 3
            nx, ny = nx + dx[d], ny + dy[d]

    if new_graph[nx][ny]:
        if new_graph[nx][ny][2]<z : new_graph[nx][ny] = [s,d,z]
    else : new_graph[nx][ny] = [s,d,z]
    graph[x][y] = []

R,C,M = map(int, input().split())
graph = [[[] for _ in range(C)] for _ in range(R)]
for i in range(M):
    r,c,s,d,z = map(int, input().split())
    graph[r-1][c-1] += [s,d,z]
fishKing = 0

# 낚시왕은 0부터 시작해서 C가 될때까지 움직인다.
# 낚시왕이 위치하는 곳을 j로 갖는 상어중 가장 위에 있는 놈을 없앤다. : for문으로 i만 증가시켜서 하나라도 없애면 break하도록
# 상어이동함수
#### 주의점! (r,c)는 (1,1)부터 시작
answer = 0
while fishKing < C :
    for i in range(len(graph)):
        if graph[i][fishKing]:
            answer += graph[i][fishKing][2]
            graph[i][fishKing] = []
            break
    new_graph = [[[] for _ in range(C)] for _ in range(R)]
    for i in range(len(graph)):
        for j in range((len(graph[0]))):
            if graph[i][j] : shark_move(i,j)
    graph = deepcopy(new_graph)
    fishKing+=1
print(answer)
