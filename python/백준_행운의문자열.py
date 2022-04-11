from itertools import permutations
s = input()

s_perm_list = permutations(s)

new_s_set = set()
for p in s_perm_list:
    new_s_set.add(''.join(p))

answer = 0
for new_s in new_s_set:
    check = True
    for i in range(len(new_s)-1):
        if new_s[i]==new_s[i+1]:
            check = False
            break
    if check :
        answer+=1
print(answer)
