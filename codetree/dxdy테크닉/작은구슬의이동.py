import sys

input = sys.stdin.readline

n, t = map(int, input().split())

r, c, dir = input().split()

r, c = int(r), int(c)

dir_num = 0
dxs, dys = [0, 1, -1, 0], [1, 0, 0, -1]

if dir == 'U':
    dir_num = 2
elif dir == 'D':
    dir_num = 1
elif dir == 'L':
    dir_num = 3
else:
    dir_num = 0

def in_range(x, y):
    return 1 <= x and x <= n and 1 <= y and y <= n

while t > 0:
    nr, nc = r + dxs[dir_num], c + dys[dir_num]
    if not in_range(nr, nc):
        dir_num = 3 - dir_num
        t -= 1
        continue
    
    r, c = r + dxs[dir_num], c + dys[dir_num]
    t -= 1

print(r, c)