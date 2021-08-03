import sys

input = sys.stdin.readline

N = int(input())

x = y = 0

def move(x, y, dir, num):
    if dir == 'N':
        nx, ny = x, y+num
    elif dir == 'S':
        nx, ny = x, y-num
    elif dir == 'E':
        nx, ny = x+num, y
    else:
        nx, ny = x-num, y
    
    return nx, ny

for i in range(N):
    dir, num = input().split()
    num = int(num)

    x, y = move(x, y, dir, num)

print(x, y)