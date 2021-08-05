import sys

input = sys.stdin.readline

n, m = map(int, input().split())

arr = [ [0 for _ in range(m)] for _ in range(n) ]
visited = [ [0 for _ in range(m)] for _ in range(n) ]

dxs, dys = [0, 1, -1, 0], [1, 0, 0, -1]
dir_num = 0
x = y = 0

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m

def change_dir(dir_num):
    if dir_num == 0:
        dir_num = 1
    elif dir_num == 1:
        dir_num = 3
    elif dir_num == 2:
        dir_num = 0
    else:
        dir_num = 2

    return dir_num

cnt = 1

# 처음부분 0,0 에서 방문표시 및 번호를 적어줌
visited[x][y] = 1
arr[x][y] = cnt

for i in range(n):
    for j in range(m):
        if cnt == n*m:
            break
        nx, ny = x + dxs[dir_num], y + dys[dir_num]
        if (not in_range(nx, ny)) or (visited[nx][ny] == 1): # 범위에 없거나, 방문했을 때 방향을 바꿈
            dir_num = change_dir(dir_num)
        x, y = x + dxs[dir_num], y + dys[dir_num]
        visited[x][y] = 1
        cnt += 1
        arr[x][y] = cnt


for i in range(n):
    for j in range(m):
        print(arr[i][j], end=" ")
    print()