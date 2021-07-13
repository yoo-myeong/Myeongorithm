# 제한사항
# 기둥의 조건 : 바닥위 or 보의 한쪽 끝에 위치 or 다른 기둥 위에 위치
# 보의 조건 : (한쪽끝이 기둥위에 위치 or 양쪽 끝이 다른 보와 연결상태) and 바닥에는 설치안됨
# 설치할때와 삭제할 때 모두 규칙을 만족시켜야함
# 만족안되면 해당 작업은 무시하고 다음 작업으로 넘어감

def check(answer):
    for ans in answer:
        x,y,a = ans
        if a == 0:
            if y==0 or [x,y,1] in answer or [x-1,y,1] in answer or [x,y-1,0] in answer:
                continue
            else:
                return False
        else:
            if y!=0:
                if [x,y-1,0] in answer or [x+1,y-1,0] in answer or ([x-1,y,1] in answer and [x+1,y,1] in answer):
                    continue
                else:
                    return False
                
    return True

def solution(n, build_frame): # 작업순서 build_frame 형태 : [x,y,a,b] 
    # [x,y,a] 형태로 반환
    answer = []
    
    # x,y는 작업 좌표 / a는 0은기둥, 1은 보 / b는 0은 삭제, 1은 설치
    for frame in build_frame:
        x,y,a,b = frame
        
        if b == 0:
            answer.remove([x,y,a])
            if not check(answer):
                answer.append([x,y,a])
        else:
            answer.append([x,y,a])
            if not check(answer):
                answer.remove([x,y,a])
    answer.sort()
    return answer
