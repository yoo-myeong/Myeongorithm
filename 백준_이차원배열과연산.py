# 열dl 클 때는, 왼쪽으로 회전시키고 행에 대해 진행 후 다시 오른쪽으로 회전해서 반환
# 0은 무시해야 함을 주의

def rotate_left(graph):
    new_graph = [[0]*len(graph) for _ in range(len(graph[0]))]
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            new_graph[len(graph[0])-j-1][i] = graph[i][j]
    return new_graph

def rotate_right(graph):
    new_graph = [[0]*len(graph) for _ in range(len(graph[0]))]
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            new_graph[j][len(graph)-i-1] = graph[i][j]
    return new_graph

def list_calculate(graph):
    max_length = -1e9
    new_graph = []
    for i in range(len(graph)):
        h = {}
        for val in graph[i]:
            if val == 0 : continue
            if val in h : h[val] += 1
            else : h[val] = 1
        sorted_list = sorted(h.items(), key=lambda x:(x[1],x[0]))
        new_line = []
        for num, cnt in sorted_list:
            new_line.append(num)
            new_line.append(cnt)
        new_graph.append(new_line)
        if len(new_line)>100 : new_line = new_line[0:100]
        max_length = max(len(new_line), max_length)
    for i in range(len(new_graph)):
        for _ in range(max_length- len(new_graph[i])): new_graph[i].append(0)
    return new_graph

r,c,k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(3)]
time = 0
while True:
    if len(graph)>=r and len(graph[0])>=c:
        if graph[r - 1][c - 1] == k: break
    if time >= 101 :
        time =-1
        break
    time += 1
    if len(graph)>= len(graph[0]): graph = list_calculate(graph)
    else:
        graph = rotate_left(graph)
        graph = list_calculate(graph)
        graph = rotate_right(graph)
print(time)
