# 뱀이 자기자신이나 벽이랑 부딪히면 끝
# 뱀이 이동후에 사과를 먹으면 길이를 유지
# 그렇지 않으면 자신의 꼬리를 한칸 소모
# 몇 초에 게임이 끝나는지 출력
from collections import deque

n = int(input())

k = int(input())

box = [[0]*n for _ in range(n)]

for i in range(k):
  x,y = map(int, input().split())
  box[x-1][y-1] = 1

l = int(input())

d = deque()

for i in range(l):
  x,c = input().split()
  x = int(x)
  d.append((x,c))

print(d)

q = deque()
q.append((0,0))

# 동 남 서 북
dir = 0
da = [0,1,0,-1]
db = [1,0,-1,0]

x,c = d.popleft()
now = 0
a,b = 0,0
box[a][b] = 3

while True:
  print(box)
  na = a+da[dir]
  nb = b+db[dir]
  print(na,nb)
  if 0<=na<n and 0<=nb<n and box[na][nb]!=3:
    if box[na][nb] == 1:
      box[na][nb] = 3
    else:
      box[na][nb] = 3
      i,j = q.popleft()
      box[i][j] = 0
    q.append((na,nb))
    a=na
    b=nb
    now += 1
    print(q)
  else:
    now+=1
    break

  # 방향변환 구현
  if now == x:
    if c == 'D':
      dir += 1
      dir %= 4
    else :
      dir += 3
      dir %= 4
    if d:
      x,c = d.popleft()

  
  print(" ")

print(now)
