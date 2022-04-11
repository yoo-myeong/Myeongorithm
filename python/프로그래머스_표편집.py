# 범위를 벗어나지 않은 행선택이 있다. 
# 몇칸 위 또는 몇카 아래를 선택하거나 현재 행을 삭제 후 아래행을 선택, 가장 최근에 삭제된 행을 복구하는 명령어가 있다.
# 마지막이 선택된상태에서 삭제하면 선택포인트는 그 윗행이 된다.
# 삭제동작이 일어날 때 선택 포인트는 가만히 있는다.

def solution(n, k, cmd):
    answer = ''
    node = {0:[n-1, 1], n-1:[n-2,0]}
    for i in range(1,n-1): node[i] = [i-1, i+1]
    stack = []
    for c in cmd:
        if len(c)>1: # U 또는 D 명령어 인 경우
            direction, step = c.split(' ')
            if direction == "D":
                for _ in range(int(step)):
                    k = node[k][1]
            else:
                for _ in range(int(step)):
                    k = node[k][0]
        else:
            if c == "C":
                prev_, next_ = node[k]
                node[prev_][1] = node[k][1]
                node[next_][0] = node[k][0]
                stack.append([k, node[k]])
                tmp = node[k]
                del node[k]
                
                if tmp[1] == 0: k = tmp[0]
                else : k = tmp[1]
            elif c == "Z":
                key, val = stack.pop()
                prev_, next_ = val
                node[key] = val
                node[prev_][1] = key
                node[next_][0] = key
    
    for i in range(n):
        if i in node: 
            answer+='O'
        else : 
            answer+='X'
    return answer
