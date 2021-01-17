import sys
input = sys.stdin.readline

N = int(input())
result = []

for i in range(N):
    x,y = map(int, input().split())
    result.append([x,y])

result = sorted(result, key=lambda x:(x[1],x[0]))

for i in result:
    print(i[0], i[1])