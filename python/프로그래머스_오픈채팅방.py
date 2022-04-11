# 닉네임 변경시 출입안내문의 닉네임도 모두 변경
# 중복 닉네임이 허용되기 때문에 변경될 것을 정확하게 구분
# (유저아이디,출입)의 튜플을 큐에 저장, 유저아이디의 닉네임을 갱신하는 해시 생성

from collections import deque    

def solution(record):
    answer = []
    record_q = deque()
    nickname = {}
    
    for r in record:
        r_split = list(r.split())
        # 들어오는 경우 큐에 (아이디, 출입) 튜플을 삽입하고, 닉네임해시 갱신(없으면 자동으로 생성)
        if r_split[0] == "Enter":
            record_q.append((r_split[1], r_split[0]))
            nickname[r_split[1]] = r_split[2]
        elif r_split[0] == "Leave":
            record_q.append((r_split[1], r_split[0]))
        elif r_split[0] == "Change":
            nickname[r_split[1]] = r_split[2]
    
    while record_q:
        userID, state = record_q.popleft()
        if state == "Enter": answer.append(nickname[userID]+"님이 들어왔습니다.")
        else : answer.append(nickname[userID]+"님이 나갔습니다.")
    
    return answer
