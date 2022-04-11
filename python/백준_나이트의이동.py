from typing import List, Tuple
from collections import deque

t :int = int(input())

ls :List[int] = []
starts : List[Tuple[int]] = []
ends : List[Tuple[int]] = []

for _ in range(t):
    ls.append(int(input()))
    starts.append(tuple(map(int, input().split())))
    ends.append(tuple(map(int, input().split())))

##########

dxy = [(-1,-2), (-2,-1), (-2,1), (-1,2), (1,2), (2,1), (2,-1), (1,-2)]

def solution(l:int, start:Tuple[int], end:Tuple[int]):
    graph :List[List[bool]] = [[False]*l for _ in range(l)]
    start_x,start_y = start
    graph[start_x][start_y] = True

    q = deque()
    q.append((start_x,start_y,0))

    while q:
        x,y,cnt = q.popleft()
        if (x,y) == end:
            return cnt
        for i in range(8):
            nx, ny = x+dxy[i][0], y+dxy[i][1]
            if 0<=nx<l and 0<=ny<l:
                if graph[nx][ny] == False:
                    graph[nx][ny] = True
                    q.append((nx,ny,cnt+1))

for i in range(t):
    l,start,end = ls[i], starts[i], ends[i]
    print(solution(l,start,end))
