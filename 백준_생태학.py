from typing import Dict, List

trees :List[str] = []
while True:
    try:
        trees.append(input())
    except:
        break

###################

dic :Dict[str, int] = {}
for t in trees:
    if dic.get(t):
        dic[t] += 1
    else:
        dic[t] = 1

length = len(trees)
new_trees :List[str] = list(dic)
new_trees.sort()

for t in new_trees:
    v = dic[t] / length
    print(t, '%.4f' % (v*100))
    
'''
소수점 반올림의 방법의 차이로 틀렸다.
https://docs.python.org/ko/3/library/functions.html?highlight=round#round
round(2.675, 2)는 2.68이 아닌 2.67을 반환한다.
십진 소수가 float으로 정확히 표현될 수 없기 때문이다.

따라서 .f를 사용해야 한다.
'''
