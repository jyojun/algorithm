import sys

input = sys.stdin.readline

arr = list(map(int, input().split()))

max_result = 0
min_result = 1001

for i in range(len(arr)):
    # 500 미만이고, max_result 보다 크면 업데이트
    if arr[i] < 500:
        if arr[i] > max_result:
            max_result = arr[i]

    else:
        if arr[i] < min_result:
            min_result = arr[i]

print(max_result, min_result) 