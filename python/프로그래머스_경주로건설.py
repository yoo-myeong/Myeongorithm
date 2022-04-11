from collections import deque

def solution(board):
    def bfs(start_dir):
        dx,dy = [-1,1,0,0],[0,0,-1,1] #북남서동
        length = len(board)
        visited = [[1e9]*length for _ in range(length)]
        visited[0][0] = 0
        
        q = deque()
        q.append([0,0,0,start_dir])
        while q:
            x,y,c,d = q.popleft()
            for i in range(4):
                nx,ny = x+dx[i], y+dy[i]
                
                if 0<=nx<length and 0<=ny<length:
                    if board[nx][ny] == 0:
                        nc = c+100 if i == d else c+600
                        if nc<visited[nx][ny]:
                            visited[nx][ny] = nc
                            q.append([nx,ny,nc,i])
        return visited[-1][-1]
    return min(bfs(1), bfs(3))
        
    return answer
