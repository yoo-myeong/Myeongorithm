# 맞닿은 국가끼리 L <= 인구 차 <= R 이면 인구 공유
# 인구공유하는 국가는 각각 ( 인구합 // 국가 수 ) 만큼 인구를 나눠갖는다
# 인구이동이 며칠동안 발생하는지 프로그램 작성
from collections import deque

n,l,r = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

# 한 국가의 이웃에 연합국이 있는지 본다
# 연합국이 있으면 지역리스트에 추가한다.
# num : [지역리스트] 를 team_table 해시테이블에 추가한다.
# key를 리스트로 뽑아서 인구를 재배치 시킨다.
# 해시를 초기화 한다.
# 반복

def team_check(x,y):
    q = deque()
    q.append((x,y))
    team = []
    check_box[x][y] = 1
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<n and check_box[nx][ny]==0:
                gap = abs(graph[x][y]-graph[nx][ny])
                if l<=gap<=r:
                    team.append((nx,ny))
                    q.append((nx,ny))
                    check_box[nx][ny] = 1
    return team

cnt = 0

while True:
    team_table = {}
    check_box = [[0] * n for _ in range(n)]

    num = 0
    for i in range(n):
        for j in range(n):
            if check_box[i][j] == 0:
                team_list = team_check(i,j)
                if len(team_list) != 0:
                    team_list.append((i,j))
                    team_table[num] = team_list
                    num+=1
    keys = list(team_table.keys())

    if len(keys) == 0:
        break

    for key in keys:
        team_list = team_table[key]

        sum_team = 0
        for x,y in team_list:
            sum_team += graph[x][y]

        people = sum_team // len(team_list)
        for x,y in team_list:
            graph[x][y] = people

    cnt += 1

print(cnt)