import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
q = deque()

grid = [ list(map(int,input().split())) for _ in range(n) ]
visited = [ [ 0 for _ in range(m) ] for _ in range(n) ]

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m

def can_go(x,y):

    if in_range(x,y) == False:
        return False
    
    if visited[x][y] == 1 or grid[x][y] == 0:
        return False
    
    return True

def bfs():

    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            if can_go(nx, ny):
                q.append([nx, ny])
                visited[nx][ny] = 1

# 시작을 (0,0) 에서 시작
q.append([0, 0])
visited[0][0] = 1

bfs()

print(visited[n-1][m-1])