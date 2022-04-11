# 절댓값이 가장 크면 됨
# 문자 숫자 분리
### ""에 숫자를 계속 +, 숫자가 아닌 것이 나오면 숫자는 정수변환, 숫자, 문자 순서대로 express_list에 삽입, 연산자는 calculation_set에 삽입
# 우선순위 순열만들기
### 연산자집합을 리스트로 변환한 뒤 순열로 우선순위 경우의 수 모음 만들기
## max_val선언
### 순열집합 for문 원소1(우선순위) : for문 원소2(연산자) , express_list을 for문 : 원소2와 같으면 현,좌,우 계산해서 우에 삽입
## 첫번째 for문 끝단에 max_val 비교 후 갱신
from itertools import permutations
from copy import deepcopy

def calculate(x,y,c):
    if c == "+": sum_val = x+y
    elif c == "*" : sum_val = x*y
    elif c == "-" : sum_val = x-y
    return sum_val

def solution(expression):
    answer = 0
    express_list = []
    calculation_set = set()
    num = ""
    for x in expression:
        if x.isdigit():num+=x
        else:
            number = int(num)
            num = ""
            express_list.append(number)
            express_list.append(x)
            calculation_set.add(x)
    number = int(num)
    express_list.append(number) # 분리 완성new_express_list
    # print(express_list) #[100, '-', 200, '*', 300, '-', 500, '+', 20]
    calculater_perm_list = list(permutations(list(calculation_set)))
    # print(calculater_perm_list) #[('*', '-', '+'), ('*', '+', '-'), ('-', '*', '+'), ('-', '+', '*'), ('+', '*', '-'), ('+', '-', '*')]
    for calculater_perm in calculater_perm_list:
        new_express_list = deepcopy(express_list)
        # print(calculater_perm)
        for calculater in calculater_perm: # calculater = * or + or -
            i = 0
            while True:
                try:
                    if new_express_list[i] == calculater:
                        sum_val = calculate(new_express_list[i-1],new_express_list[i+1],new_express_list[i])
                        new_express_list[i-1] = sum_val
                        del new_express_list[i]
                        del new_express_list[i]
                        # print(new_express_list)
                    else: i+=1
                
                except: break #인덱스를 벋어나면 break
                
        answer = max(answer, abs(new_express_list[-1]))
    
    return answer
