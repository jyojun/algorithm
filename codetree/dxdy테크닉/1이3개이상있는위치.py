import sys

input = sys.stdin.readline

N = int(input())

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
arr = [list(map(int, input().split())) for _ in range(N)]

def is_inrange(n, x, y):
    return (0 <= x and x < n) and (0 <= y and y < n)

result_cnt = 0

for i in range(N):
    for j in range(N):
        cnt = 0
        for dx, dy in zip(dxs, dys):
            nx, ny = i + dx, j + dy

            if is_inrange(N, nx, ny) and arr[nx][ny] == 1:
                cnt += 1
        
        if cnt >= 3:
            result_cnt += 1
            #print(i, j)

print(result_cnt)