from typing import List

n :int = int(input())
a,b = map(int, input().split())
m :int = int(input())

graph :List[List[int]] = [[] for _ in range(n+1)]
for _ in range(m):
    x,y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

#####################

visited = [False for _ in range(n+1)]
answer = -1

def dfs(node,cnt):
    global answer
    if node == b:
        answer = cnt
        return
    for next_n in graph[node]:
        if not visited[next_n]:
            visited[next_n] = True
            dfs(next_n, cnt+1)
            visited[next_n] = False

dfs(a, 0)
print(answer)
