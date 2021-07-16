# 1시간동안 취약지점이 모두 점검될 수 있는 최소 친구수
# 먼저 친구를 내보낼 순서를 정한다
# 각 경우의 수에 대하여, 첫번째 친구를 원의 처음부터 마지막 지점까지 배치시켜보면서 그때마다의 필요한 친구수로 최솟값을 비교, 갱신한다.
# 첫번째 친구를 마지막 지점에 위치시켰을 경우 그 다음 위치는 n부터 n+n까지 이므로 확인할 지점을 추가로 설치 -> 지점 + n 하면 된다.

from itertools import permutations

def solution(n, weak, dist): 
    length = len(weak)
    for i in range(length):
        weak.append(weak[i]+n)
        
    answer = len(dist)+1
    for friend in list(permutations(dist, len(dist))):
        for start in range(length):
            position = weak[start]+friend[0]
            count = 1
            for i in range(start, start+length):
                if position<weak[i]:
                    
                    count+=1
                    if count > len(dist):
                        break
                    position = weak[i] + friend[count-1]
            answer = min(count, answer)
        
    if answer > len(dist):
        return -1
    return answer
