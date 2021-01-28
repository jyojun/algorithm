import sys
input = sys.stdin.readline

K = int(input())

stack = []
sum = 0
for i in range(K):
    num = int(input())

    if num > 0: # 1~9일 경우
        stack.append(num)
        sum += num
    else: # 0일경우
        temp = stack.pop()
        sum -= temp

print(sum)