# column 번호가 짝수일 경우 row가 증가, 홀수일 경우 row가 감소

import sys

input = sys.stdin.readline

N, M = map(int, input().split())

arr = [[0 for _ in range(M)] for _ in range(N)]
cnt = 0
row, column = 0, 0

for i in range(N):
    for j in range(M):
        arr[row][column] = cnt
        cnt += 1
        if column % 2 == 0:
            if row == N-1:
                column += 1
            else:
                row += 1

        else:
            if row == 0:
                column += 1
            else:
                row -= 1

#print(arr)

for i in range(N):
    for j in range(M):
        print(arr[i][j], end=" ")
    print()