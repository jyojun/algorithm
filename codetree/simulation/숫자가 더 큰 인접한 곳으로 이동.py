import sys

input = sys.stdin.readline

n, x, y = map(int,input().split())
x, y = x-1, y-1

grid = [ list(map(int,input().split())) for _ in range(n) ]

result = []
result.append(grid[x][y])

dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1] # 상하좌우 우선순위 순서

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

def is_possible(x, y):
    for i in range(4):
        nx, ny = x + dxs[i], y + dys[i]
        if in_range(nx, ny) and grid[x][y] < grid[nx][ny]:
            return True
    
    return False

while(is_possible(x,y)):
    for i in range(4):
        nx, ny = x + dxs[i], y + dys[i]
        if in_range(nx, ny) and grid[x][y] < grid[nx][ny]:
            result.append(grid[nx][ny])
            x, y = x + dxs[i], y + dys[i]
            break

for i in range(len(result)):
    print(result[i], end=" ")