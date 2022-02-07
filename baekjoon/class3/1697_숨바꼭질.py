import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
min_step = [0 for _ in range(10**5)]

def bfs():
    q = deque()
    q.append(N)

    while q:
        x = q.popleft()
        if x == K:
            print(min_step[x])
            break
        for nx in (x-1, x+1, x*2):
            #print(nx)
            
            # nx가 범위에 들어가고, 방문하지 않았을 때
            if 0 <= nx and nx <= 10**5 and min_step[nx] == 0:
                min_step[nx] = min_step[x] + 1
                q.append(nx)

bfs()