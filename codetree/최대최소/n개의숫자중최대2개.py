import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

max_val = arr[0]

for i in range(N):
    if max_val < arr[i]:
        max_val = arr[i]

max_val2 = arr[0]

for i in range(N):
    if max_val2 < arr[i]:
        if arr[i] == max_val:
            continue
        else:
            max_val2 = arr[i]

print(max_val, max_val2)