# 크기가 큰 물고기가 있는 곳은 갈 수 없음
# 크기가 같은 물고기가 있는 곳은 먹지 않고 정착
# 크기가 작은 물고기는 먹고 정착, 자신의 크기와 같은 걸 먹었을 때만 아기상어는 1 성장

from collections import deque
n = int(input()) # 최대 400
graph,baby,fishes = [],[],[]
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] == 9 : baby = [i,j]
        elif 1<=graph[i][j]<=6 : fishes.append((i,j,graph[i][j]))
# print(baby)
# for x in fishes: print(x)
babyHeight = 2
# bfs로 상어보다 작은 물고기 중 가까운 애들 탐색해서 후보자 생성하는 함수 생성
## 주의할 건 물고기가 자기보다 클 때만 못지나감. 같으면 지나갈 수 있음
def bfs(i,j):#상어좌표 대입
    q = deque()
    q.append((i,j,0))
    dx, dy, minCount, closer_min_fishes, Isfirst = [-1,1,0,0], [0,0,-1,1], 1e9, [], True
    visited = [[False]*n for _ in range(n)]
    while q:
        x,y,cnt = q.popleft()
        cnt+=1
        if cnt == minCount+1: # 가장 가까이 있는 놈의 거리를 넘어서면 탐색 불필요
            break
        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]
            if 0<=nx<n and 0<=ny<n:
                if visited[nx][ny] == False:
                    visited[nx][ny] = True
                    if graph[nx][ny] < babyHeight and graph[nx][ny]!=0:
                        if Isfirst :
                            Isfirst = False
                            minCount = cnt
                        closer_min_fishes.append((nx,ny))
                    if graph[nx][ny] <= babyHeight:
                        q.append((nx,ny,cnt))
    closer_min_fishes.append(minCount)
    return closer_min_fishes

# while반복
# 후보자 생성, 존재하지 않으면 break
# 후보자를 상하, 좌우 순서로 정렬해서 0번째것 사용
answer = 0
EatingTimes = 0
baby_i, baby_j = baby
while True:
    closer_min_fishes = bfs(baby_i, baby_j)
    # print(closer_min_fishes) #########################
    cnt = closer_min_fishes.pop()
    if not closer_min_fishes: break
    answer += cnt
    closer_min_fishes = sorted(closer_min_fishes, key=lambda x:(x[0], x[1]))
    # print(closer_min_fishes[0]) #########################
    new_x, new_y = closer_min_fishes[0]
    graph[new_x][new_y] = 0
    graph[baby_i][baby_j] = 0
    baby_i, baby_j = new_x, new_y
    EatingTimes+=1
    if EatingTimes == babyHeight:
        babyHeight +=1
        EatingTimes = 0

print(answer)
