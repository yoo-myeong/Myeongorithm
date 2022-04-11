from copy import deepcopy

def rotate(num, dir):
    rotate_state = [0,0,0,0]
    rotate_state[num] = dir

    rx,lx = num, num
    while rx<3:
        if graph[rx][2] != graph[rx+1][6] :
            rotate_state[rx+1] = rotate_state[rx]*-1
            rx+=1
        else : break
    while lx>0:
        if graph[lx][6] != graph[lx-1][2]:
            rotate_state[lx-1] = rotate_state[lx]*-1
            lx-=1
        else : break
    new_graph = deepcopy(graph)
    for i in range(4):
        if rotate_state[i] ==1:
            new_graph[i][1:9] = graph[i][0:8]
            new_graph[i][0] = graph[i][7]
        elif rotate_state[i] == -1:
            new_graph[i][0:7] = graph[i][1:8]
            new_graph[i][7] = graph[i][0]
    return new_graph

graph = []
for i in range(4):
    graph.append(list(input()))
# for x in graph: print(x)
rotate_times = int(input())

for _ in range(rotate_times):
    num, direction = map(int, input().split())
    graph = rotate(num-1, direction)

answer = 0
if graph[0][0] == '1' : answer+=1
if graph[1][0] == '1' : answer+=2
if graph[2][0] == '1' : answer+=4
if graph[3][0] == '1' : answer+=8

print(answer)
