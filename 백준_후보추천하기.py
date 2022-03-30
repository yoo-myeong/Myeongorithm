from typing import List, Dict

n :int = int(input())
m :int = int(input())
students :List[int] = map(int, input().split())

###################################################################################

def solution(n:int, m:int, students:List[int]) -> List[int] : 
    answer:List[int] = []

    photos :Dict[int, List[int]] = {}

    def removeOneStudent() : 
        remove_num :int = None
        min_cnt :int = 1e9
        min_idx :int = 1e9

        for num in photos:
            idx, cnt = photos[num]
            
            if min_cnt > cnt:
                min_cnt = cnt
                min_idx = idx
                remove_num = num
            elif min_cnt == cnt and min_idx > idx:
                min_idx = idx
                remove_num = num
        
        del photos[remove_num]

    for num in students:
        length = len(photos)
        
        if photos.get(num):
                photos[num][1] += 1

        else : 
            if length < n :
                photos[num] = [length, 1]
            elif length >= n :
                removeOneStudent()
                photos[num] = [length, 1]

    answer = list(photos.keys())
    answer.sort()

    return answer

###################################################################################

for x in solution(n,m,students):
    print(x, end = " ")
