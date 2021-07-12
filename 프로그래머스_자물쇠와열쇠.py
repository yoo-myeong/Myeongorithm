# 열쇠 회전 이동
# 자물쇠와 겹치는 열쇠부분의 돌기가 자물쇠의 홈에 들어가면 열림
# 돌기와돌기가 만나는 건 금지
# key와 lock은 0과 1을 홈과 돌기로 나타낸 배열
# 결과 : 자물쇠를 열 수 있으면 True, 없으면 False

# 키를 회전하고, 자물쇠에 처음 겹치는 순간부터 마지막 겹치는 순간까지 이동시킨다
# 그러기 위해서 먼저 자물쇠를 3배로 늘리면 계산하기 편함
# 각 경우에 자물쇠에 겹쳐진 열쇠의 값을 더했는데 전체 자물쇠의 값이 1이면 True

def rotate(a):
    col = len(a)
    row = len(a[0])
    
    # result는 col과 row가 반대
    result = [[0]*col for _ in range(row)]
    
    for i in range(row):
        for j in range(col):
            result[i][j] = a[j][row-i-1]
    
    return(result)

# 자물쇠 열리는지 확인
def check(lock):
    k = len(lock)//3
    for i in range(k,k*2):
        for j in range(k,k*2):
            if lock[i][j] !=1:
                return False
    return True

def solution(key, lock):
    # 3배키운 자물쇠 new_lock 생성
    x = len(lock)
    new_lock = [[0] * (x * 3) for _ in range(x * 3)]
    for i in range(x):
        for j in range(x):
            new_lock[x+i][x+j] = lock[i][j]
    
    #4가지 방향 확인
    for _ in range(4):
        key = rotate(key)
        # 이동시킬 경우의 수
        for a in range(x*2):
            for b in range(x*2):
                # 자물쇠와 열쇠 합치기
                for i in range(len(key)):
                    for j in range(len(key)):
                        new_lock[a+i][b+j] += key[i][j]
                
                if check(new_lock) == True:
                    return True
                
                # 자물쇠가 안 열린 경우 자물쇠 다시 원상복구
                
                for i in range(len(key)):
                    for j in range(len(key)):
                        new_lock[a+i][b+j] -= key[i][j]
                        
    return False
