# 상하좌우 = 0,1,2,3 일때 0,2,1,3
from copy import deepcopy

def getDragonCurve(k,d):
    move = [d]
    for _ in range(k):
        temp = []
        for i in range(len(move)):
            temp.append((move[-i - 1] + 1) % 4)
        move.extend(temp)
    return move

n = int(input())
graph = [[0]*101 for _ in range(101)]
dy, dx = [0,-1,0,1],[1,0,-1,0]
for _ in range(n):
    x,y,d,k = map(int, input().split())
    graph[x][y] = 1
    dirList = getDragonCurve(k,d)
    for dir in dirList:
        x,y = x+dx[dir], y+dy[dir]
        graph[x][y] = 1

answer=0
for i in range(100):
    for j in range(100):
        if graph[i][j] == 1:
            if graph[i+1][j]==1 and graph[i][j+1]==1 and graph[i+1][j+1]==1:
                answer+=1
print(answer)
