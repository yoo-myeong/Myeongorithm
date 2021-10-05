from collections import deque

n,m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(input()))
    for j in range(m):
        if graph[i][j] == "R" : red = [i,j]
        if graph[i][j] == "B" : blue = [i,j]

# 공을 멈출 때 까지 움직이기
def move(x,y,dx,dy):
    time = 0
    while graph[x+dx][y+dy]!="#":
        if graph[x+dx][y+dy] == 'O': return (False,False,0)
        x,y,time = x+dx, y+dy, time+1
    return x,y,time

def bfs():
    visit = {}
    q = deque([red+blue])
    visit[(red[0],red[1],blue[0],blue[1])] = 0
    while q:
        rx,ry,bx,by = q.popleft()
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nrx,nry,rtime = move(rx,ry,dx,dy)
            nbx,nby,btime = move(bx,by,dx,dy)
            if (nbx,nby) == (False, False): continue
            elif (nrx,nry) == (False, False) : return visit[rx,ry,bx,by]+1
            elif (nrx,nry) == (nbx,nby) :
                if rtime>btime : nrx,nry = nrx-dx, nry-dy
                else : nbx,nby = nbx-dx, nby-dy
            if (nrx,nry,nbx,nby) not in visit:
                visit[(nrx,nry,nbx,nby)] = visit[rx,ry,bx,by]+1
                q.append([nrx,nry,nbx,nby])
        if visit[rx,ry,bx,by] >=10: return -1
    return -1

print(bfs())
