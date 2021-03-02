import sys

input = sys.stdin.readline

dp = [0,1,2,4] 

T = int(input())

for i in range(T):
    n = int(input())

    for i in range(4,11):
        dp.append(dp[i-1]+dp[i-2]+dp[i-3])
    print(dp[n])