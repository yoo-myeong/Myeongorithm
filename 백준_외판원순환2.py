from typing import List

n = int(input())
graph :List[List[int]] = [list(map(int, input().split())) for _ in range(n)]

###########
answer = 1e9
visited :List[bool] = [False for _ in range(n)]

def dfs(start :int, node :int, cnt :int, cost :int):
    global answer
    if cnt == n and graph[node][start] != 0:
        answer = min(answer, cost+graph[node][start])
        return
    for i in range(n):
        if visited[i] == False and graph[node][i] != 0:
            visited[i] = True
            dfs(start, i ,cnt+1, cost+graph[node][i])
            visited[i] = False

for i in range(n):
    visited[i] = True
    dfs(i,i,1,0)
    visited[i] = False

print(answer)
