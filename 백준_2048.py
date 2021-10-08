from copy import deepcopy

def rotate_left(graph):
    new_graph = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n): new_graph[n-j-1][i] = graph[i][j]
    return new_graph

def rotate_right(graph):
    new_graph = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n): new_graph[j][n-i-1] = graph[i][j]
    return new_graph

def rotate_flip(graph):
    new_graph = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n): new_graph[i][n-j-1] = graph[i][j]
    return new_graph

def move_way(graph): # 왼쪽으로 몰아넣는 동작
    for i in range(len(graph)):
        point = 0
        for j in range(1,len(graph[0])):
            point_num, checking_num = graph[i][point], graph[i][j]
            if checking_num == 0: continue # 일단 확인하는 곳이 0이면 패스
            if point_num == checking_num : # 대기칸과 확인칸이 같은 숫자면
                graph[i][point] *= 2
                graph[i][j] = 0
                point +=1
            else: # 대기칸과 확인칸이 다른 숫자면
                if point_num == 0: # 대기칸이 빈칸이면 그대로 들어감
                    graph[i][point] = checking_num
                    graph[i][j] = 0
                else: # 빈칸이아니면 그 옆칸으로 들어감
                    graph[i][j] = 0
                    graph[i][point+1] = checking_num
                    point += 1

def move(dir,graph):# dir 좌우상하
    if dir == 0:move_way(graph)
    elif dir == 1:
        graph = rotate_flip(graph)
        move_way(graph)
        graph = rotate_flip(graph)
    elif dir == 2:
        graph = rotate_left(graph)
        move_way(graph)
        graph = rotate_right(graph)
    elif dir == 3:
        graph = rotate_right(graph)
        move_way(graph)
        graph = rotate_left(graph)
    return graph

max_val = -1e9
def dfs(tmp_graph, time):
    global max_val
    if time == 5:
        for i in range(n):
            for j in range(n): max_val = max(max_val, tmp_graph[i][j])
        return
    origin_copy = deepcopy(tmp_graph)
    for i in range(4):
        new_graph = move(i, tmp_graph)
        dfs(new_graph,time+1)
        tmp_graph = deepcopy(origin_copy)

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

dfs(graph,0)
print(max_val)
