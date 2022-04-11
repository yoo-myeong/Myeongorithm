from typing import List, Dict

n :int = int(input())
arr :List[int] = list(map(int, input().split()))

#########

arr_filtered :List = list(set(arr))
arr_filtered.sort()
# print(arr_filtered)

d :Dict[int, int] = {}
for i, val in enumerate(arr_filtered):
    d[val] = i

for i in range(n):
    print(d[arr[i]], end=" ")
    
'''
- 각 인덱스는 자신의 값보다 작은 값이 중복을 제외하고 몇개 있는가를 새로운 값으로 갖는다.
- 중복은 set을 사용해서 없앤다.
- 중복을 제외한 자신보다 작은값의 개수는 중복을 제거한 리스트를 정렬했을 때 자신의 인덱스와 같다.
  - 예를 들어 [-10, -9, 2, 4, 8] 로 중복이 제거된 리스트를 정렬했을 때 값이 4일경우 그 보다 작은 값은 -10, -9, 2로 총 3개이며 이는 4라는 값이 가지는 인덱스의 번호와 일치한다.
- { 값 : 인덱스 } 를 dictionary로 만들고, arr을 순차탐색해서 사전형을 통과시켜 새 좌표값을 얻는다.
'''
