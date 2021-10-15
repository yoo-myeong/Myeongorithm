##### 실제로 회전시키고 그 중 작은 값들을 append하는 것을 반복

# q를 오른쪽 한칸 회전후 다시 우하좌상for문에 q.popleft()값을 삽입
# 이때 min_val을 뽑아서 answer append
from collections import deque
def solution(rows, columns, queries):
    answer = []
    graph,num = [[] for _ in range(rows)],1
    for i in range(rows):
        for j in range(columns):
            graph[i].append(num)
            num+=1
    
    for x1,y1,x2,y2 in queries:
        # 주어진 좌표에 있는 값을 우하좌상순으로 q에 삽입
        x1,y1,x2,y2 = x1-1,y1-1,x2-1,y2-1
        q = deque()
        for k in range(y1,y2+1): q.append(graph[x1][k])
        for k in range(x1+1,x2+1): q.append(graph[k][y2])
        for k in range(y2-1,y1-1,-1): q.append(graph[x2][k])
        for k in range(x2-1,x1,-1): q.append(graph[k][y1])
        q.rotate(1)
        answer.append(min(q))
        for k in range(y1,y2+1): graph[x1][k] = q.popleft()
        for k in range(x1+1,x2+1): graph[k][y2] = q.popleft()
        for k in range(y2-1,y1-1,-1): graph[x2][k] = q.popleft()
        for k in range(x2-1,x1,-1): graph[k][y1] = q.popleft()
    
    return answer
