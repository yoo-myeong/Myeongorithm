# 주사위 처음 상태 : 윗면이 1, 동쪽은 3
# 칸에쓰인 수가 주사위의 바닥면으로 이동. 칸은 0이됨
# 칸이 원래 0이면 주사위바닥값이 칸으로 복사됨.(주사위바닥면값 유지)
# 주사위가 이동될 때 마다 상단에 있는 값을 출력

n,m,x,y,k = map(int, input().split())

graph = []
for i in range(n): graph.append(list(map(int, input().split())))
direction_commmand = list(map(int, input().split()))

# 동서북남 순서로 바뀔 인덱스를 표기 # 1씩 빼줘야 dice의 인덱스
dice_status = [[4,2,1,6,5,3],[3,2,6,1,5,4],[5,1,3,4,6,2],[2,6,3,4,1,5]]

def dice_move(direction, dice):
    new_dice = []
    for dice_i in dice_status[direction]: #[4,2,1,6,5,3]
        new_dice.append(dice[dice_i-1])
    return new_dice

dice = [0]*6

dx = [0,0,-1,1]
dy = [1,-1,0,0]

for direction in direction_commmand:#4 4 4 1 3 3 3 2
    nx,ny = x+dx[direction-1], y+dy[direction-1]
    if 0<=nx<n and 0<=ny<m:
        x,y = nx,ny
        dice = dice_move(direction-1, dice)
        if graph[x][y] == 0:
            graph[x][y] = dice[5]
        else:
            dice[5] = graph[x][y]
            graph[x][y] = 0
        print(dice[0])

