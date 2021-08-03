import sys

input = sys.stdin.readline

start, end = map(int, input().split())
count = 0
for i in range(start, end+1):
    sum = 0
    for j in range(1, i+1):
        if i != j: # 마지막 자기 자신 제외
            if i % j == 0: # 나누어 떨어지는 경우(약수)
                sum += j
    if i == sum:
        #print(i)
        count += 1

print(count)