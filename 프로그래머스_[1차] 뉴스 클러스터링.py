# 자카드 유사도 = 교집합 크기 / 합집합 크기
# 중복값 유의
# 대문자와 소문자를 같게 취급
# 최종 유사도에 65536을 곱해서 출력

##### 풀이
# 두개씩 끊어서 .upper()해준 뒤 리스트에 삽입
# (합집합 = 전체개수 - 교집합)이므로
### 교집합구하기
# 이중반복문과 visited사용해서 교집합 구하기

def solution(str1, str2): # 2<= <=1000
    answer = 0
    s1_list = []
    s2_list = []
    
    for i in range(0,len(str1)-1):
        s = str1[i].upper()+str1[i+1].upper()
        if s.isalpha():
            s1_list.append(s) #	['FR', 'RA', 'AN', 'NC', 'CE']
    for i in range(0,len(str2)-1):
        s = str2[i].upper()+str2[i+1].upper()
        if s.isalpha():
            s2_list.append(s) # ['FR', 'RE', 'EN', 'NC', 'CH']
    #print(s1_list)
    #print(s2_list)
    
    share_cnt = 0 # 교집합 개수
    visited = [False]*len(s2_list)
    for s1 in s1_list:
        for s2_i in range(len(s2_list)):
            if s1 == s2_list[s2_i]:
                if visited[s2_i] == False:
                    visited[s2_i] = True
                    share_cnt += 1
                    break
    
    sum_cnt = len(s1_list) + len(s2_list) - share_cnt
    #print("share", share_cnt)
    #print("sum", sum_cnt)
    if share_cnt == 0 and sum_cnt == 0:
        answer = 1
    else:
        answer = share_cnt / sum_cnt
            
    return int(answer*65536)
