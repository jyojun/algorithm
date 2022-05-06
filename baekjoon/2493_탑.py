import sys

input = sys.stdin.readline

n = int(input())
t = list(map(int, input().split()))
tops = [[t[i], i+1] for i in range(n)]
tops.reverse()
result = []

for i in range(n-1):
    cnt = 0
    for j in range(i+1, n):
        if tops[i][0] < tops[j][0]:
            result.append(tops[j][1])
            # print('여기 부딪힘', tops[i][0], tops[j][0])
            cnt += 1
            break
    if cnt == 0:
        result.append(0)
result.append(0)
print(result)
