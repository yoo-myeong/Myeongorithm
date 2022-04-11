n,m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

Tetromino_list = [
    [(0, 0), (0, 1), (1, 0), (1, 1)],
    [(0, 0), (0, 1), (0, 2), (0, 3)],
    [(0, 0), (1, 0), (2, 0), (3, 0)],
    [(0, 0), (0, 1), (0, 2), (1, 0)],
    [(1, 0), (1, 1), (1, 2), (0, 2)],
    [(0, 0), (1, 0), (1, 1), (1, 2)],
    [(0, 0), (0, 1), (0, 2), (1, 2)],
    [(0, 0), (1, 0), (2, 0), (2, 1)],
    [(2, 0), (2, 1), (1, 1), (0, 1)],
    [(0, 0), (0, 1), (1, 0), (2, 0)],
    [(0, 0), (0, 1), (1, 1), (2, 1)],
    [(0, 0), (0, 1), (0, 2), (1, 1)],
    [(1, 0), (1, 1), (1, 2), (0, 1)],
    [(0, 0), (1, 0), (2, 0), (1, 1)],
    [(1, 0), (0, 1), (1, 1), (2, 1)],
    [(1, 0), (2, 0), (0, 1), (1, 1)],
    [(0, 0), (1, 0), (1, 1), (2, 1)],
    [(1, 0), (0, 1), (1, 1), (0, 2)],
    [(0, 0), (0, 1), (1, 1), (1, 2)]
]

answer = 0
for x in range(n):
    for y in range(m):
        for Tetromino in Tetromino_list: #Tetromino: [(0, 0), (0, 1), (1, 0), (1, 1)]
            sum_val = 0
            check = True
            for i in range(4):
                dx, dy = Tetromino[i]
                nx, ny = x+dx, y+dy
                if 0<=nx<n and 0<=ny<m:sum_val += graph[nx][ny]
                else :
                    check=False
                    break
            if check : answer = max(answer, sum_val)

print(answer)
