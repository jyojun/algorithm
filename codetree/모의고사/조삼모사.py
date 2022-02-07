import sys

input = sys.stdin.readline

N = int(input())

grid = [ 
    list(map(int,input().split()))
    for _ in range(N)
]

cnt = 0
result = []

def divide(x, i, arr):

    if (i == N-1):
        return
    if (len(arr) == N // 2):
        result.append(arr)

    divide(0, i+1, arr)
    arr.append(i)
    divide(1, i+1, arr)

divide(0, 0, [])
print(result)