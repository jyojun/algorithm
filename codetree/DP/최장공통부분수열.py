import sys

grid = [list(input()) for _ in range(2)]

grid[0] = list('#') + grid[0]
grid[1] = list("#") + grid[1]

dp = [
    [0 for _ in range(len(grid[1])+1)] 
    for _ in range(len(grid[0])+1)
]

if grid[0][1] == grid[1][1]:
    dp[1][1] = 1
else:
    dp[1][1] = 0

# initialization
for i in range(2, len(grid[0])+1):
    if grid[0][i] == grid[1][1]:
        dp[i][1] = 1
    else:
        dp[i][1] = dp[i - 1][1]

for i in range(2, len(grid[1])+1):
    if grid[1][i] == grid[0][1]:
        dp[1][i] = 1
    else:
        dp[1][i] = dp[1][i - 1]

for i in range(2, len(grid[0])+1):
    for j in range(2, len(grid[1])+1):
        if grid[0][i] == grid[1][j]:
            dp[i][j] = dp[i - 1][j - 1] + 1

        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(dp[len(grid[0])][len(grid[0])])
print(dp)