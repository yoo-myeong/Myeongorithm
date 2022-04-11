def tornado_num(n):
    graph = [[0]*n for _ in range(n)]
    num_point_list = [(n//2,n//2)]
    rotate_time = n*2 # 마지막 한번은 방향만 틀어서 같은 칸 반복
    dx,dy, dir = [0,1,0,-1], [-1,0,1,0],0 # 좌하우상
    x,y = n//2, n//2
    for i in range(rotate_time-2):
        for j in range(i//2+1):
            x, y = x+dx[dir], y+dy[dir]
            num_point_list.append((x,y))
        dir = (dir+1)%4
    for j in range((n-1)):
        tmp = graph[x][y]
        x, y = x + dx[dir], y + dy[dir]
        num_point_list.append((x, y))
    return num_point_list

def destroy(di,si):
    x,y = n//2, n//2
    dx,dy = [0,-1,1,0,0],[0,0,0,-1,1]
    for _ in range(si):
        x,y = x+dx[di],y+dy[di]
        graph[x][y] = 0

def pull():
    emptyNum = False
    for i in range(1,len(num_point_list)):
        x,y = num_point_list[i]
        if graph[x][y] == 0 and emptyNum == False:  emptyNum = i
        elif graph[x][y]!=0 and emptyNum != False:
            nx,ny = num_point_list[emptyNum]
            graph[nx][ny] = graph[x][y]
            graph[x][y] = 0
            emptyNum+=1

def bomb():
    global answer
    bombed = False
    now_repeat_list = set()
    repeat_list = []
    for i in range(1,len(num_point_list)-1):
        x,y = num_point_list[i]
        nx,ny = num_point_list[i+1]
        if graph[x][y] == graph[nx][ny]:
            now_repeat_list.update([(x,y),(nx,ny)])
        else:
            now_repeat_list = list(now_repeat_list)
            if len(now_repeat_list)>=4:
                repeat_list += list(now_repeat_list)
            now_repeat_list = set()
    for x,y in repeat_list:
        bombed = True
        answer += graph[x][y]
        graph[x][y] = 0
    return bombed

def change_graph():
    h, point = 1,1
    new_graph = [[0]*n for _ in range(n)]
    repeating = False
    for i in range(1,len(num_point_list)):
        if point >= (len(num_point_list) - 1): break
        x,y = num_point_list[i]
        if i == (len(num_point_list)-1):
            px, py = num_point_list[point]
            npx, npy = num_point_list[point + 1]
            new_graph[px][py], new_graph[npx][npy] = h, graph[x][y]
            break
        nx,ny = num_point_list[i+1]
        if graph[x][y] == 0 :break
        if graph[nx][ny] == graph[x][y]:
            if repeating: h+=1
            else : h = 2
            repeating = True
        else:
            if point>=(len(num_point_list)-1):break
            px,py = num_point_list[point]
            npx,npy = num_point_list[point+1]
            if repeating : new_graph[px][py], new_graph[npx][npy] = h, graph[x][y]
            else: new_graph[px][py], new_graph[npx][npy] = 1, graph[x][y]
            repeating,h = False,1
            point += 2
    return new_graph

answer = 0
n,m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
num_point_list = tornado_num(n)
for t in range(m):
    di,si = map(int, input().split())
    destroy(di,si)
    pull()
    while True:
        if not bomb(): break
        pull()
    graph = change_graph()

print(answer)
