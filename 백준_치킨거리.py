# 집을 기준으로 가장 가까운 치킨집까지의 거리
# 거리는 |r1-r2| + |c1-c2|로 구한다.
# 치킨거리 총합이 최소가 되도록 M개의 치킨집만 남기고 나머지는 0으로 만들어 도시의 치킨거리를 구하라
from itertools import combinations

n,m = map(int, input().split())

box = []
houses = []
chickens = []

for i in range(n):
  a = list(map(int, input().split()))
  box.append(a)

for i in range(n):
  for j in range(n):
    if box[i][j] == 1:
      houses.append((i,j))
    elif box[i][j] == 2:
      chickens.append((i,j))

cases = list(combinations(chickens, m))

result = 1e9

for case in cases:
  sum = 0

  for house in houses:
    a = 1e9
    x1,y1 = house

    for chicken in case:
      x2,y2 = chicken
      b = abs(x2-x1)+abs(y2-y1)
      a = min(a,b)

    sum += a

  result = min(result, sum)

print(result)
