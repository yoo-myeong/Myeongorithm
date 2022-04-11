import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
s = input()

########################################

answer = 0
repeatCnt = 0
i = 1

while i<m-1:
    if s[i-1:i+2] == "IOI":
        repeatCnt += 1
        if repeatCnt == n:
            answer += 1
            repeatCnt -= 1
        i+=1
    else:
        repeatCnt = 0
    i+=1

print(answer)
