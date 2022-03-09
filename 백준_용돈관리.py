from typing import List

n,m = map(int, input().split())
pays :List[int] = [int(input()) for _ in range(n)]

################

def getCnt(outCost:int)->int:
    cnt = 1
    sum = 0
    for pay in pays:
        sum += pay
        if sum > outCost:
            cnt+=1
            sum = pay
    return cnt


left, right = max(pays), sum(pays)
answer = 1e9

while left<=right:
    mid = (left+right)//2
    cnt = getCnt(mid)
    if cnt <= m:
        answer = min(answer, mid)
        right = mid-1
    else:
        left = mid+1

print(answer)
