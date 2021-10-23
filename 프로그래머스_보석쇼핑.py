# 모든종류가 1개 이상포함되게 구간을 쓸어담는 것 중 가장 짧은 구간

def solution(gems):
    answer = []
    min_distance = 1e9
    
    start, end = 0, 0
    treasure_cnt = {}
    treasure_set_len = len(set(gems))
    
    while end<len(gems):
        if gems[end] not in treasure_cnt: treasure_cnt[gems[end]] = 1
        else : treasure_cnt[gems[end]] += 1
        end += 1
        
        if len(treasure_cnt) == treasure_set_len:
            while start<end:
                if treasure_cnt[gems[start]] > 1:
                    treasure_cnt[gems[start]]-=1
                    start += 1
                else : 
                    break
            if min_distance > (end-start):
                min_distance = (end-start)
                answer = [start+1, end]
            
    return answer
