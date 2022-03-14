from typing import List,Tuple

t :int = int(input())
ns :List[int] = []
costs :List[List[int]] = []

for _ in range(t):
    ns.append(int(input()))
    costs.append(list(map(int, input().split())))

###########

def solution(n :int, cost:List[int])->int:
    max_v :int = cost[-1]
    answer = 0
    for i in range(len(cost)-2, -1, -1):
        if(max_v > cost[i]):
            answer += (max_v-cost[i])
        else:
            max_v = cost[i]
    return answer

for i in range(t):
    print(solution(ns[i], costs[i]))
    
'''
원래 방식을 뒤집어버리는 생각에 유연해져야겠다.
'''
