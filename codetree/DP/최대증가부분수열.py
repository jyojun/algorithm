import sys

input = sys.stdin.readline

N = int(input())

given_seq = list(map(int, input().split()))

a = [0 for _ in range(N+1)]
a[1:] = given_seq[:]
dp = [-1 for _ in range(N+1)]

dp[0] = 0
for i in range(1,N+1):
    for j in range(i):
        if a[i] > a[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))