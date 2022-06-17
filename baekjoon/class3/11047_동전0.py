import sys

input = sys.stdin.readline

n, k = map(int, input().split())

coins = [int(input()) for _ in range(n)]

coins.sort(reverse=True)
cnt = 0

for i in coins:
    if k == 0:
        break
    cnt += k // i
    k %= i

print(cnt)
