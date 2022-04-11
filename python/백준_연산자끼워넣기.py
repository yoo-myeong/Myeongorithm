from itertools import permutations

n = int(input()) #수의 개수

num = list(map(int, input().split()))
# n개, 순서유지

sign_num = list(map(int, input().split()))
# 연산자 4개의 각각의 개수, 숫자사이 끼워서 사칙연산 무시하여 계산

#모든 연산 결과중 최댓값과 최솟값 계산

signs = []
count = 1
for i in sign_num:
    for j in range(i):
      signs.append(count)
    count+=1


sign_set = list(permutations(signs, n-1))

cnt=1
maxi = -1e9
mini = 1e9
for sign in sign_set:
  sum = num[0]
  cnt+=1
  for cal in range(len(sign)):
    if sign[cal] == 1:
      sum += num[cal+1]
    elif sign[cal] == 2:
      sum-= num[cal+1]
    elif sign[cal] == 3:
      sum *= num[cal+1]
    elif sign[cal] == 4:
      if sum <0:
        sum*=-1
        sum //= num[cal+1]
        sum*=-1
      else:
        sum //= num[cal+1]      
  maxi = max(sum, maxi)
  mini = min(sum, mini)

print(maxi)
print(mini)
