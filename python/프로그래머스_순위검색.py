# 효율성 모두 탈락

python_set,java_set,cpp_set,backend_set,frontend_set,junior_set,senior_set,chicken_set,pizza_set = set(),set(),set(),set(),set(),set(),set(),set(),set()
grade_list = []
str_set = {
"python":python_set, "java":java_set, "cpp":cpp_set, "backend":backend_set, "frontend":frontend_set, "junior":junior_set, "senior":senior_set, "chicken":chicken_set, "pizza":pizza_set
}

def getset(info,i):
    lang, job, exp, food, grade = info[i].split()
    str_set[lang].add(i)
    str_set[job].add(i)
    str_set[exp].add(i)
    str_set[food].add(i)
    grade_list.append(grade)


def solution(info, query):
    answer = []
    for i in range(len(info)): getset(info, i) # 집합 업데이트
    
    for cmd in query:
        result_set = set([i for i in range(len(info))])
        cmd_split = cmd.split()
        for condition in cmd_split:
            if condition == "and" or condition == "-" or condition.isdigit() : continue
            result_set = result_set&str_set[condition]
        cnt = 0
        for i in result_set: 
            if int(grade_list[i]) >= int(cmd_split[-1]) : cnt+=1
        answer.append(cnt)
    return answer
