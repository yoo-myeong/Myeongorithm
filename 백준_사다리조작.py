# 한 행에 N-1개의 가로선을 배치할 수 있다, 연속으로 배치가 안됨
# h*n 행렬에서 (0,0)부터 (h,n-1)까지만 설치가 된다는 의미.

def perform_game():
    for j in range(n):
        tmp = j
        for i in range(h):
            if graph[i][tmp] == 1 : tmp+=1
            elif tmp-1>=0:
                if graph[i][tmp-1] == 1: tmp-=1
        if tmp != j : return False
    return True

candidate_points = []
answer = 1e9
def dfs(idx):
    global answer, candidate_points
    check= perform_game()
    if check: answer = min(answer, len(candidate_points))
    if len(candidate_points) == 3: return
    for i in range(idx, len(empty_point)):
        x,y = empty_point[i]
        graph[x][y] += 1
        candidate_points.append((x,y))
        dfs(i+1)
        x,y = candidate_points.pop()
        graph[x][y] -=1

n,m,h = map(int, input().split())
graph = [[0]*(n) for _ in range(h)]
for _ in range(m):
    i,j = map(int, input().split())
    graph[i-1][j-1] = 1

empty_point = []
for i in range(h):
    for j in range(n-1):
        if graph[i][j] == 0:
            empty_point.append((i,j))

dfs(0)

if answer == 1e9: print(-1)
else:print(answer)
