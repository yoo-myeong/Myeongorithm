# 실패율이 높은 스테이지부터 내림차순으로 반환
# 실패율 = 그 스테이지의 클리어못한 인원  /  스테이지에도달한전체인원

###풀이
# 1단계면 stages를 차례비교하다가 1보다 작은 숫자면 cnt +=1, 크면 break
# 실패율 계산해서 append하고 total -= cnt, now += cnt, cnt = 0
def solution(N, stages): # 스테이지 개수  /  사용자들의현재스테이지번호배열
    answer = []
    length = len(stages)
    stages.sort() # 1 2 2 2 3 3 4 6
    
    now =0
    total = length # 8
    for step in range(1,N+1): # 1부터 5까지
        cnt = 0
        
        if total == 0:
            fail = 0
            answer.append((step,0))
        else:
            for i in range(now, length): # now부터 7까지
                if stages[i] <= step:
                    cnt+=1
                else:
                    break
            fail = cnt/total
            answer.append((step,fail))
            total -= cnt 
            now += cnt 
    
    answer = sorted(answer, key=lambda x: (-x[1],x[0]))
    result = []
    for x,y in answer:
        result.append(x)
    return result
