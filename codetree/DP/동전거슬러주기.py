import sys

input = sys.stdin.readline

MAX_ANS = 10001

n, m = map(int, input().split())
coins = list(map(int, input().split()))
dp = [ MAX_ANS for _ in range(m+1) ]

# dp[i] = min(dp[i-coins[j]) + 1
dp[0] = 0
for i in range(m+1):
  for j in range(n):
    # list out of range 오류를 막기 위해서
    if i >= coins[j]:
      # 최솟값을 저장시켜 준다. 
      dp[i] = min(dp[i], dp[i-coins[j]] + 1)

if dp[m] == MAX_ANS:
  print(-1)
else:
  print(dp[m])