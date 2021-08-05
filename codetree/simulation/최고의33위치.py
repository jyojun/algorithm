import sys

input = sys.stdin.readline

N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

#print(arr)

def count_coin(arr, x, y):
    cnt = 0
    for i in range(3):
        for j in range(3):
            if arr[x+i][y+j] == 1:
                cnt += 1
    
    return cnt

result = []
for i in range(N-2):
    for j in range(N-2):
        result.append(count_coin(arr, i, j))

print(max(result))