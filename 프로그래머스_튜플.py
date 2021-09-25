def solution(s): # s는 10만개면 tuple은 500개? 정도 밖에 안됨
    answer = []
    
    tuple_list = []
    num = ""
    num_list = []
    openStatus = True
    for i in range(len(s)-1):
        c = s[i]
        if c.isdigit():
            num += c
        if c == "," and openStatus:
            num_list.append(int(num))
            num = ""
        elif c== "{": openStatus = True
        elif c == "}":
            num_list.append(int(num))
            num = ""
            openStatus = False
            tuple_list.append(num_list)
            num_list = []
    # print(tuple_list) #[[1, 2, 3], [2, 1], [1, 2, 4, 3], [2]]
    
    new_tuple_list = []
    tuples = set()
    for length in range(1,len(tuple_list)+1): # 1~4
        for number_set in tuple_list:
            if len(number_set) == length:
                for num in number_set:
                    if not num in tuples:
                        answer.append(num)
                        tuples.add(num)
    return answer
