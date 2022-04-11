from itertools import combinations

n,m = map(int, input().split())

box = []
empty = []


for i in range(n):
  data = list(map(int,input().split()))
  for j in range(m):
      if data[j] == 0:
          empty.append((i,j))
  box.append(data)


dx = [-1,1,0,0]
dy = [0,0,-1,1]
def virus(x,y,new_box):
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        if 0<=nx<n and 0<=ny<m:
            if new_box[nx][ny] == 0:
                new_box[nx][ny] = 2
                virus(nx,ny,new_box)

def width(box):
    result = 0
    for i in range(n):
        for j in range(m):
            if box[i][j] == 0:
                result +=1
    return result



new_block = list(combinations(empty,3))

result = 0

for block in new_block:
    new_box = [[-1]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            new_box[i][j] = box[i][j]
    for x,y in block:
        new_box[x][y] = 1

    for i in range(n):
        for j in range(m):
            if new_box[i][j] == 2:
                virus(i,j,new_box)
    result = max(result,width(new_box))

print(result)
