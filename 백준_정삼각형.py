n = int(input())

# 중간 -1,0 과 -1,-1 을 더해서 비교
# 제일 왼쪽 : j==0 , left는 +(-1,0), right는 0
# 제일 오른쪽 : i==j, left는 0, right는 +(-1,-1)

graph = []
for i in range(n):
  graph.append(list(map(int, input().split())))

for i in range(1,n):
  for j in range(len(graph[i])):
    if j == 0:
      sum_left = graph[i][j]+graph[i-1][j]
      sum_right = 0
    elif i==j:
      sum_left = 0
      sum_right = graph[i][j]+graph[i-1][j-1]
    else:
      sum_left =  graph[i][j]+graph[i-1][j]
      sum_right =  graph[i][j]+graph[i-1][j-1]
    graph[i][j] = max(sum_left, sum_right)

print(max(graph[n-1]))
