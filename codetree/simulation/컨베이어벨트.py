import sys

input = sys.stdin.readline

N, t = map(int, input().split())

arr = [ list(map(int, input().split())) for _ in range(2) ]

def in_range(r, c):
    return 0 <= r and r < 2 and 0 <= c and c < N-1

r = c = 0

for i in range(t):

    temp = arr[0][N-1]

    for j in range(N-1, 0, -1):
        arr[0][j] = arr[0][j-1]
    arr[0][0] = arr[1][N-1]

    for j in range(N-1, 0, -1):
        arr[1][j] = arr[1][j-1]
    arr[1][0] = temp

for i in range(2):
    for j in range(N):
        print(arr[i][j], end=" ")
    print()