from collections import deque
def bfs(x,y,graph):
    q=deque()
    q.append((x,y,0))
    dx,dy = [-1,1,0,0], [0,0,-1,1]
    possible = True
    visited = [[False]*5 for _ in range(5)]
    while q:
        x,y,cnt = q.popleft()
        visited[x][y] = True
        if cnt>=3:
            break
        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]
            if 0<=nx<5 and 0<=ny<5:
                if graph[nx][ny] !="X" and visited[nx][ny] == False:
                    if graph[nx][ny] == "O":
                        q.append((nx,ny,cnt+1))
                        visited[nx][ny] = True
                    elif graph[nx][ny] == "P":
                        if (cnt+1)<=2:
                            possible = False
                            break
        if not possible:
            break
    return possible
                        
    
def solution(places):
    answer = []
    for place in places:
        graph = []
        for pox in place:
            graph.append(list(pox))
        graph_possible = True
        for i in range(5):
            for j in range(5):
                if graph[i][j] == "P": graph_possible = bfs(i,j,graph)
                if not graph_possible: break
            if not graph_possible: break
        if graph_possible: answer.append(1)
        else: answer.append(0)
                    
    return answer
