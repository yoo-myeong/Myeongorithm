# dfs로 블록그룹짓기 0은 무한히 포함가능, 그룹은 시작점을 키로, 그것의 리스트를 값 저장
# 블록체크 끝날 때마다 max값 비교해서 max면 max_point에 좌표 저장도 같이해주기
# max_point를 해시에 넣어서 값에 있는 point들 전부 제거

from collections import deque
def rotate_left(graph):
    new_graph = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new_graph[n-j-1][i] = graph[i][j]
    return new_graph
def rotate_rigth(graph):
    new_graph = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new_graph[j][n-i-1] = graph[i][j]
    return new_graph
def move_right(graph):
    for i in range(n):
        for j in range(n-1,-1,-1):
            if graph[i][j] != -1 and graph[i][j] !='.':
                nj,tmp = j, graph[i][j]
                while True:
                    nj+=1
                    if 0<=nj<n:
                        if graph[i][nj]=='.': graph[i][nj-1], graph[i][nj] = '.', tmp
                        else: break
                    else: break
    return graph
def bfs(graph): # 제거할 블록 리스트를 반환
    max_val, max_group_list, dx, dy =2, [], [-1,1,0,0],[0,0,-1,1]
    visited = [[False]*n for _ in range(n)]
    zero_point = [(i,j) for i in range(n) for j in range(n) if not graph[i][j]]
    for i in range(n):
        for j in range(n):
            for zero_x, zero_y in zero_point: visited[zero_x][zero_y] = False
            if graph[i][j] != '.' and  graph[i][j] != 0 and graph[i][j] != -1:
                if not visited[i][j]: # 그룹체크가 안된 좌표일 경우
                    rainbow_cnt = 0
                    tmp,visited[i][j] = graph[i][j], True
                    q=deque()
                    q.append((i,j))
                    group = [(i,j)]
                    cnt = 1
                    while q:
                        x,y  = q.popleft()
                        for d in range(4):
                            nx,ny = x+dx[d], y+dy[d]
                            if 0<=nx<n and 0<=ny<n:
                                if not visited[nx][ny]:
                                    if graph[nx][ny] == tmp or graph[nx][ny] == 0:
                                        if graph[nx][ny] == 0 : rainbow_cnt+=1
                                        visited[nx][ny], cnt = True, cnt+1
                                        group.append((nx,ny))
                                        q.append((nx,ny))
                    group.append(rainbow_cnt)
                    max_group_list.append(group)
    max_group_list = sorted(max_group_list, key=lambda x: (-x[-1],-x[0][0],-x[0][1]))
    max_group_list = sorted(max_group_list, key=len, reverse=True)
    # print(max_group_list) # [(0, 0), (0, 1), 1], [(1, 0), (2, 0), (2, 1), 0],...
    if max_group_list : return max_group_list[0]
    else : return [False]

n,m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
answer = 0
while True:
    max_group = bfs(graph)
    rainbow_cnt = max_group.pop()
    # print(max_group)#####################################################
    # print(len(max_group),"-----max group-------")  ######################################
    if len(max_group) <= 1: break # 그룹이 없다는 뜻이므로 종료
    else : answer+= len(max_group)**2
    for x,y in max_group: graph[x][y] = '.' # 가장 큰 그룹 제거
    # for f in graph: print(f)##############################################
    # print("-----remove-------")######################################
    graph = rotate_left(graph)
    # for f in graph: print(f)##############################################
    # print("-----rotate left-------")######################################
    graph = move_right(graph)
    # for f in graph: print(f)##############################################
    # print("-----move rigth-------")######################################
    graph = rotate_left(graph)
    # for f in graph: print(f)##############################################
    # print("-----rotate left-------")######################################
    graph = move_right(graph)
    # for f in graph: print(f)##############################################
    # print("-----move rigth-------")######################################
    graph = rotate_rigth(graph)
    # for f in graph: print(f)##############################################
    # print("-----rotate right-------")######################################
print(answer)

# n = 4
# graph = [
#     [1,0,'.',0],
#     [2,'.',-1,1],
#     [0,2,-1,'.'],
#     [1,1,1,'.']
# ]
# bfs(graph)
