# p를 올바른 괄호문자열로 바꾸는 작업
# 각 작업을 함수로 만들어서 순서대로 진행
# step2는 (와 )가 처음으로 갯수가 딱 맞아질 때를 u로 넣고 나머지를 v로 분리
#step3는 )갯수가 (를 넘어가면 false 통과하면 true


def step2(text):
    cnt1 = 0
    cnt2 = 0
    if text[0] == '(':
        cnt1+=1
    else:
        cnt2+=1
        
    for i in range(1, len(text)):
        if text[i] =='(':
            cnt1 += 1
        else:
            cnt2 += 1
            
        if cnt1==cnt2:
            return i

def step3(text):
    cnt1 = 0
    cnt2 = 0
    for i in text:
        if i == '(':
            cnt1 +=1
        else:
            cnt2 +=1
        if cnt2>cnt1:
            return False
    return True

def remove_reverse(text):
    result = ""
    for i in range(1,len(text)-1):
        if text[i] == '(':
            result += ')'
        else:
            result += '('
    return result

def solution(p):
    answer = ''
    if len(p) == 0:
        return p
    len_u = step2(p)
    u = p[0:len_u+1]
    v = p[len_u+1:len(p)]
    if step3(u):
        answer = u+solution(v)
    else:
        answer = '(' + solution(v) + ')' + remove_reverse(u)
    return answer
