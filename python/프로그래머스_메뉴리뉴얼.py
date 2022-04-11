# 2가지 이상의 메뉴, 최소 2명이상이 주문한 조합
##### 풀이
# 코스를 for문 => 원소1
# order for문 => 원소2, 원소2에서 원소1 만큼의 묶음을 갖는 조합을 구해서 set에 add
# set을 리스트로 변환, 갯수저장리스트에 같은인덱스의 개수를 저장, max구해서 그 값과 같은 조합만 꺼내서 result에 append

from itertools import combinations

def solution(orders, course): # 주문기록, 신코스메뉴갯수 / 2~20, 2~10
    answer = []
    for dishes in course:
        set_order_combi = set()
        order_combi = []
        for order in orders:
            combi_list = list(combinations(order, dishes)) # dishes만큼 묶이는 조합을 리스트로 만들어서
            # 중복 가능한 리스트와
            for c in combi_list:
                c = sorted(c)
                order_combi.append(tuple(c))
            # 중복 불가한 집합에 넣기
            set_order_combi.update(order_combi) 
        ########## ("order_combi",list(order_combi))
        if not order_combi : continue # 만들어진 조합이 하나도 없으면 continue
        list_set_order_combi = list(set_order_combi)
        ########## ("list_set_order_combi",list_set_order_combi)
        cnt_order_combi = [0]*len(list_set_order_combi) # 집합의 인덱스의 갯수를 저장
        for i in range(len(list_set_order_combi)):
            cnt_order_combi[i] = int(order_combi.count(list_set_order_combi[i]))
        ########## ("cnt_order_combi",cnt_order_combi)
        max_cnt = max(cnt_order_combi)
        ########## ("max_cnt", max_cnt)
        
        # max_cnt의 인덱스를 가진 조합을 answer에 삽입
        if max_cnt != 1: # 두번 이상 주문해야만 넣기로 했으므로
            for i in range(len(cnt_order_combi)):
                if cnt_order_combi[i] == max_cnt:
                    answer.append("".join(list_set_order_combi[i]))
    answer = sorted(answer)
    
    return answer
