from collections import deque
import sys

input = sys.stdin.readline
def bfs():
    q = deque()
    q.append((A,""))
    visited[A] = True
    while q:
        q_A, cmd = q.popleft()
        if q_A == B:
            return cmd

        len_now = len(str(q_A))

        new_A = (q_A*2)%bound
        if not visited[new_A]:
            visited[new_A] = True
            q.append((new_A, cmd+'D'))

        new_A = (q_A-1) % bound
        if not visited[new_A]:
            visited[new_A] = True
            q.append((new_A, cmd + 'S'))

        front = q_A % 1000
        back = q_A // 1000
        new_A = front*10+back
        if not visited[new_A]:
            visited[new_A] = True
            q.append((new_A, cmd + 'L'))

        front = q_A % 10
        back = q_A // 10
        new_A = front * 1000 + back
        if not visited[new_A]:
            visited[new_A] = True
            q.append((new_A, cmd + 'R'))

t = int(input())
bound = 10000
for i in range(t):
    A, B = map(int, input().split())
    visited = [False]*bound
    print(bfs())
