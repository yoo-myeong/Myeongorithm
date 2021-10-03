# 칸후보리스트를 채운다(인접칸에 좋아하는 사람이 max인 칸으로)
# len(칸후보리스트)!=1이면 sorted(x[0],[1]) 진행
# 0번원소에 학생을 배치

n = int(input())
Like_student_graph = [[] for _ in range((n*n)+1)]
student_line = []
for i in range(n*n):
    LikeInfo = list(map(int, input().split()))
    Like_student_graph[LikeInfo[0]] = LikeInfo[1:]
    student_line.append(LikeInfo[0])

graph = [[0]*n for _ in range(n)]

def getProfer(num):
    candidate_list = [] # 1번조건
    max_like_student_cnt = 0
    for x in range(n): # 각 칸에 들어갔을 때 주위에 몇명있는 지 체크
        for y in range(n):
            now_cnt,blank_cnt,dx,dy = 0,0,[-1,1,0,0],[0,0,-1,1]
            if graph[x][y] != 0: continue
            for i in range(4): # 4방향 체크
                nx,ny = x+dx[i], y+dy[i]
                if 0<=nx<n and 0<=ny<n:
                    if graph[nx][ny] == 0:blank_cnt+=1
                    if graph[nx][ny] in Like_student_graph[num]: now_cnt+=1
            # 현재칸이 가장 많은 학생수면 후보 갱신
            if now_cnt>max_like_student_cnt :
                candidate_list, max_like_student_cnt = [(x,y,blank_cnt)], now_cnt
            # 현재칸이 max와 같으면 후보에 추가
            elif now_cnt == max_like_student_cnt: candidate_list.append((x,y,blank_cnt))
    #
    candidate_list = sorted(candidate_list, key=lambda x: (-x[2],x[0],x[1]))
    return (candidate_list[0][0],candidate_list[0][1])

for num in student_line:
    x,y = getProfer(num)
    graph[x][y] = num

answer = 0
for x in range(n):
    for y in range(n):
        cnt,  dx, dy, num = 0, [-1, 1, 0, 0], [0, 0, -1, 1], graph[x][y]
        for i in range(4):  # 4방향 체크
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] in Like_student_graph[num]: cnt += 1
        if cnt == 0 : continue
        elif cnt == 1 : answer+=1
        elif cnt == 2: answer += 10
        elif cnt == 3 : answer+=100
        elif cnt == 4 : answer+= 1000

print(answer)
