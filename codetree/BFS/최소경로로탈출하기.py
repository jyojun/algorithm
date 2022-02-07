import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
q = deque()

grid = [ list(map(int,input().split())) for _ in range(n) ]
visited = [ [ 0 for _ in range(m) ] for _ in range(n) ]
min_step = [ [ 0 for _ in range(m) ] for _ in range(n) ]

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

cnt = 1

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m

def can_go(x,y):

    if in_range(x,y) == False:
        return False
    
    if visited[x][y] == 1 or grid[x][y] == 0:
        return False
    
    return True

def bfs():
    global cnt

    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            if can_go(nx, ny):
                q.append([nx, ny])
                visited[nx][ny] = 1
                min_step[nx][ny] = min_step[x][y] + 1

q.append([0,0])
visited[0][0] = 1

bfs()

#print(min_step)

if min_step[n-1][m-1] == 0:
    print(-1)
else:
    print(min_step[n-1][m-1])