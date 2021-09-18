# 조망권이 확보된 세대 수
 
# 리스트 for문으로 현재 인덱스의 -1, +1의 원소가 현재 원소보다 작으면 answer+=1
# 인덱스가 0일 경우 +1만 확인, 인덱스가 n-1인 경우 -1만 확인
# 10번 반복
 
def building_check(building_list):
    answer = 0
    for i in range(2,len(building_list)-2):
        right_1 = building_list[i] - building_list[i + 1]
        right_2 = building_list[i] - building_list[i + 2]
        left_1 = building_list[i] - building_list[i - 1]
        left_2 = building_list[i] - building_list[i - 2]
        if i == 2:
            if right_1 > 0 and right_2>0:
                answer += min(right_1,right_2)
        elif i == len(building_list)-3:
            if left_1 >0 and left_2 > 0:
                answer += min(left_1, left_2)
        else:
            if right_1 > 0 and right_2>0 and left_1 >0 and left_2 > 0:
                answer += min(right_1, right_2, left_1, left_2)
    return answer
 
for test_case_num in range(1,11):
    n = int(input())
    building_list = list(map(int, input().split()))
    print("#"+str(test_case_num), building_check(building_list))
