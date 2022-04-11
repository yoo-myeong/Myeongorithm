# 1개이상 모음, 2개이상 자음이 포함하여 오름차순 정렬
# C개 중 L개의 순열만들기
# 순열 만들기
# 순열 for문으로 집합에 넣기
# 집합을 리스트로 변환하고 오름차순 정렬해서 제출해보기
# 안되면 heapq사용

import heapq
from itertools import combinations

l,c = map(int, input().split())
password_candidates = input().split()

pw_perm = combinations(password_candidates, l)
# print(list(pw_perm))

heap = []
for pw in pw_perm:
    pw = ''.join((sorted(pw)))
    heapq.heappush(heap, pw)

for _ in range(len(heap)):
    pw = heapq.heappop(heap)
    m, j = 0, 0
    for c in pw:
        if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
            m+=1
        else:
            j+=1
    if m>=1 and j>=2:
        print(pw)
