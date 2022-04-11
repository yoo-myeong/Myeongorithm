from typing import List
from itertools import combinations

cases :List[List[int]] = []
while True:
    data :str = input()
    if data == "0" : break
    data_split = list(data[2:].split())
    cases.append(data_split)
# print(cases)

############

for case in cases:
    for result in combinations(case, 6):
        print(" ".join(result))
    print()
