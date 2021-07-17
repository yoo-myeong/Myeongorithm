from collections import deque

n,m,k,x = map(int, input().split())
# x가 출발점. 최단거리가 k인 모든 도시를 오름차순으로 출력
graph = [[] for _ in range(n+1)]
dist = [-1]*(n+1)
dist[x] = 0

for i in range(m):
  a,b = map(int, input().split())
  graph[a].append(b)
result = []
q = deque()
q.append(x)

while q:
  now = q.popleft()
  distance = dist[now]
  for i in graph[now]:
    if dist[i]==-1:
      dist[i] = distance+1
      q.append(i)
      if dist[i] == k:
        result.append(i)

result.sort()
if len(result) == 0:
  print(-1)
else:
  for i in range(len(result)):
    print(result[i])
