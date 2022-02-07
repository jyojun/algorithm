import sys

input = sys.stdin.readline

N = int(input())

stairs = [ int(input()) for _ in range(N) ]
dp = []
dp.append(stairs[0])

if(N >= 2):
    dp.append(max(stairs[0]+stairs[1], stairs[1]))
if(N >= 3):
    dp.append(max(stairs[0]+stairs[2], stairs[1]+stairs[2]))

if(N >= 4):
    # 3번째 부터
    for i in range(3, N):
        # 직전에서 온 경우(그 전, 그자리 점수 + 그전전전 자리까지 최대 점수) or 그 전전에서 온 경우(그 전전에서 왔을 때 최대점수 + 그자리 점수)
        dp.append(max(stairs[i] + stairs[i-1] + dp[i-3], stairs[i] + dp[i-2])) # 

print(dp[-1])