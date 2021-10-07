from collections import deque

def NoRemove(graph):
    sum_val = 0
    sum_cnt = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0:
                sum_cnt +=1
                sum_val += graph[i][j]
    if sum_val == 0: return
    avg = sum_val / sum_cnt
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0 : continue
            if graph[i][j] > avg : graph[i][j]-=1
            elif graph[i][j] < avg : graph[i][j]+=1

def remove(graph):
    remove_list = set()
    for i in range(n):
        for j in range(-1,m-1):
            if graph[i][j] != 0:
                if graph[i][j] == graph[i][j+1] :
                    remove_list.add((i,j))
                    remove_list.add((i,j+1))
    for j in range(m):
        for i in range(n-1):
            if graph[i][j]!=0:
                if graph[i][j] == graph[i+1][j] :
                    remove_list.add((i,j))
                    remove_list.add((i+1,j))

    for x,y in remove_list: graph[x][y] = 0
    if not remove_list : NoRemove(graph)

def rotate(i,di,ki):
    q=deque()
    for v in graph[i]: q.append(v)
    if di == 0 :
        q.rotate(ki)
    if di == 1:
        q.rotate(-ki)
    return q

n,m,t = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
for p in range(t):
    xi,di,ki = map(int, input().split())
    for i in range(len(graph)):
        if (i+1)%xi == 0:
            q = rotate(i,di,ki)
            new_line = []
            for data in q: new_line.append(data)
            graph[i] = new_line
    remove(graph)
sum_val = 0
for i in range(n): sum_val += sum(graph[i])
print(sum_val)
