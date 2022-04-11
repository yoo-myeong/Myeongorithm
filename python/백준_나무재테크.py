# 봄 : 칸에서 어린나무순으로 양분을 먹음, 나이만큼 양분을 먹지못한 나무는 바로 사망, 양분먹고는 나이 1증가
# 여름 : 죽은 나무의 나이를 2로 나눈값이 그 칸의 양분으로 추가됨
# 가을 : 나이가 5의배수인 나무에 인접한 8개칸에 나이가 1인 나무 태어남
# 겨울 : 로봇이 돌아다니면서 양분 추가

n,m,k = map(int, input().split()) # N:크기, M: 나무갯수, K년 후 총 나무 개수
graph = [[5]*n for _ in range(n)] # 토지의 양분 박스
extra = [list(map(int, input().split())) for _ in range(n)] # 매년추가되는 양분 양
trees = [[[] for _ in range(n)] for _ in range(n)] # 0이면 나무없음
for i in range(m):
    x,y,z = map(int, input().split()) # 주의 (1,1)부터 시작
    trees[x-1][y-1].append(z)
# for x in trees : print(x)

#k년 동안 반복
for _ in range(k):
    spreading_trees = []
    for i in range(n):
        for j in range(n):
            if trees[i][j]:
                dead_trees = []
                new_trees = []
                trees[i][j].sort()
                for tree in trees[i][j]: # 칸에 존재하는 나무 갯수만큼 인덱스 탐색
                    if graph[i][j] >= tree:
                        graph[i][j] -= tree
                        new_trees.append(tree+1) # 양분먹고 한살먹은 어린나무 새로 등록
                        if (tree+1) % 5 == 0:spreading_trees.append((i,j)) # 나이가 5배수인 나무는 가을에 번식하므로 미리 저장
                    else:
                        dead_trees.append((i,j,tree))
                trees[i][j] = new_trees # 죽거나 산 나무 리스트 갱신해서 재등록
                # 죽은 나무를 양분으로 변화시켜서 칸의 양분 갱신
                for dead_x, dead_y, dead_age in dead_trees: graph[dead_x][dead_y] += (dead_age//2)
                # 5배수 나무 번식
    dx, dy = [-1,-1,-1,0,0,1,1,1], [-1,0,1,-1,1,-1,0,1]
    for x, y in spreading_trees:
        for d in range(8):
            nx,ny = x+dx[d], y+dy[d]
            if 0<=nx<n and 0<=ny<n:
                trees[nx][ny].append(1)

    # print("가을이 끝났을 때 양분")
    # for x in graph: print(x)
    # print("-------")
    # 로봇 양분 추가
    for ri in range(n):
        for rj in range(n):
            graph[ri][rj] += extra[ri][rj]
    # print("겨울돼서 로봇이 양분 뿌리고 나서 양분표와 나무상태")
    # for x in graph : print(x)
    # print("--------")
    # for x in trees : print(x)
    # print("--------")
    # print("--------")

answer = 0
for i in range(n):
    for j in range(n):
        if trees[i][j]: answer+=len(trees[i][j])
print(answer)
