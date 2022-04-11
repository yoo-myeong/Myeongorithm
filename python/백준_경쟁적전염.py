from collections import deque

n,k = map(int, input().split())

box = []
virus = []

for i in range(n):
  x = list(map(int, input().split()))
  for j in range(n):
    if x[j] != 0:
      virus.append((x[j],i,j))
  box.append(x)
      
s,col,row = map(int, input().split())

virus.sort()

q = deque()

for v in virus:
  a,x,y = v
  q.append((a,x,y,0))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

while q:
  v,x,y,now = q.popleft()
  if now == s:
    break
  for i in range(4):
    nx = x+dx[i]
    ny = y+dy[i]

    if 0<=nx<n and 0<=ny<n:
      if box[nx][ny]==0:
        box[nx][ny] = v
        q.append((v,nx,ny,now+1))

print(box[col-1][row-1])
