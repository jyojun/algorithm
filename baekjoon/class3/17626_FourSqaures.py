import sys, math
input = sys.stdin.readline

n = int(input())

dp = [0, 1]

for i in range(2, n+1):
    count = 5
    j = 1

    while(j**2) <= i:
        count = min(count, dp[i - (j**2)])
        j += 1
    
    #print(count + 1) 
    dp.append(count + 1) # 1을 더해주는 이유는 dp[j**2] = 1 이기 때문.

print(dp[n])