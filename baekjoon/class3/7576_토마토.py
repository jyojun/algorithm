# bfs 문제 가장 멀리 있는 토마토까지 가기위해 걸리는 시간!
# 가장 멀리있는 토마토까지 가면 모든 토마토가 익는다고 확신. 

import sys
from collections import deque

input = sys.stdin.readline

def bfs(M, N, box):

    # 상하좌우
    dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]

    days = -1

    while ripe:
        days += 1
        for _ in range(len(ripe)):
            x, y = ripe.popleft()

            # 상하좌우 4번 확인 
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                # nx, ny가 박스 범위안이여야 하고, (nx, ny)위치에 안익은 박스가 있어야함
                # 익은 토마토 주위에 막혀있거나, 전부 익었다면 pass or 안익은 토마토가 있으면 익었다고 변경후, ripe에 추가
                if(0 <= nx < N) and (0 <= ny < M) and (box[nx][ny] == 0):
                    box[nx][ny] = box[nx][ny] + 1 # 안익은 -> 익은 토마토로 변경
                    ripe.append([nx,ny])
        
    for tomatoes in box:
        if 0 in tomatoes:
            return -1
    return days

M, N = map(int, input().split())

box = [list(map(int, input().split())) for _ in range(N)]
ripe = deque([])

for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            ripe.append([i,j])

print(bfs(M, N, box))



