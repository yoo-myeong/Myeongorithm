from typing import List, Set

n,d,k,c = map(int,input().split())
numbers :List[int] = [int(input()) for _ in range(n)]

#######################

answer = -1e9
for i in range(n):
    eaten : Set[int] = set()
    for j in range(k):
        idx = (i+j)%n
        eaten.add(numbers[idx])
    eaten.add(c)
    answer = max(answer, len(eaten))

print(answer)

'''
문제의 의도를 정확히 이해하지 못해서, 시간을 너무 많이 소비했음.
중복과 상관없이 k개의 접시를 먹을 경우 무조건 c 번호의 초밥을 하나 제공하는 것인데,
중복을 제외했을 때 k개의 접시를 먹을 경우에만 c번호 초밥을 제공하는 것으로 문제를 풀이해서 틀렸음.
'''
