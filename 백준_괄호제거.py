# left와 right의 인덱스 뽑기
# left의 0번째와 쌍을 이루는 것은 right은 해시로 생성
# 1부터 left의길이 만큼 left로 만드는 조합 생성 후 쌍을 지워서 문자열 생성
# 문자열 모은 리스트는 heap화 해서 뽑아내기

from itertools import combinations
import heapq
data = input()

left = [] #[0, 3]
pos = []
j=0
for i in range(len(data)):
    if data[i] == "(": left.append(i)
    elif data[i] == ")" : pos.append((left.pop(),i))

answer_list = []
for i in range(1,len(pos)+1):
    del_data_combi = combinations(pos,i) # [((3, 7),), ((0, 10),)], [((3, 7), (0, 10))]
    for del_data in del_data_combi:
        Notdel_idx = [True]*len(data)
        for idx in del_data:
            Notdel_idx[idx[0]] = False
            Notdel_idx[idx[1]] = False
        answer = ""
        for k in range(len(data)):
            if Notdel_idx[k] : answer+=data[k]
        if not answer in  answer_list:
            heapq.heappush(answer_list,answer)

for i in range(len(answer_list)):
    print(heapq.heappop(answer_list))
