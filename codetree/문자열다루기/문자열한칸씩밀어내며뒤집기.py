import sys

input = sys.stdin.readline

arr, N = map(str, input().split())

for i in range(int(N)):
    order = int(input())

    if order == 1:
        arr = arr[1:] + arr[0]
        print(arr)
    elif order == 2:
        arr = arr[-1] + arr[:-1]
        print(arr)
    else:
        arr = arr[::-1]
        print(arr)
