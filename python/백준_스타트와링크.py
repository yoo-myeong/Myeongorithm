from typing import List, Tuple, Set
from itertools import combinations

n = int(input())
graph:List[List[int]] = [list(map(int, input().split())) for _ in range(n)]

################

answer = 1e9

members = [i for i in range(n)]
members_set : Set = set(members)


cases : List[Tuple[int]] = combinations(members, n//2)
# print(list(cases))

for case in cases:
    power1 = 0
    for m1,m2 in combinations(case, 2):
        power1 += graph[m1][m2]
        power1 += graph[m2][m1]
    
    team1 = set(list(case))
    team2 : Set = members_set - team1

    power2 = 0
    for m1, m2 in combinations(list(team2), 2):
        power2 += graph[m1][m2]
        power2 += graph[m2][m1]
    
    answer = min(answer, abs(power1-power2))

print(answer)
