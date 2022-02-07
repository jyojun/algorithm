import sys

input = sys.stdin.readline

N = int(input())

grid = [ list(map(int, input().split())) for _ in range(N) ]

result = 0

dp = [ [ 0 for _ in range(N) ] for _ in range(N) ]
x,y = 0,0

dp[0][0] = grid[0][0]

# 가장 자리 초기값 세팅
for i in range(1,N):
    dp[i][0] = dp[i-1][0] + grid[i][0]
    dp[0][i] = dp[0][i-1] + grid[0][i]

for i in range(1, N):
    for j in range(1, N):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + grid[i][j]

print(dp[N-1][N-1])