# 장애물 3개를 설치해서 감시를 피할 수 있는 지 출력
# 박스는 (1,1)부터 시작

from itertools import combinations

n = int(input())

box = []
teacher = []
nothing = []

dx = [-1,1,0,0]
dy = [0,0,-1,1]
def check(x,y,newBox):
    for i in range(4):
        nx = x
        ny = y
        while True:
            nx = nx+dx[i]
            ny = ny+dy[i]
            if 0<=nx<n and 0<=ny<n and newBox[nx][ny] !='O':
                if newBox[nx][ny] == 'S':
                    return False
            else:
                break
    return True

def TecherCheck(newBox):
    for i,j in teacher:
        if not check(i,j,newBox):
            return False
    return True

for i in range(n):
    box.append(list(input().split()))
    for j in range(n):
        if box[i][j] == 'T':
            teacher.append((i,j))
        elif box[i][j] == 'X':
            nothing.append((i,j))

cases = list(combinations(nothing, 3))

possible = False
for case in cases:
    newBox = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            newBox[i][j] = box[i][j]

    for x,y in case:
        newBox[x][y] = 'O'
    if TecherCheck(newBox):
        possible = True
        break
if possible:
    print("YES")
else:
    print("NO")
