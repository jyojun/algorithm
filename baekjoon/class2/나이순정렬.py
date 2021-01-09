import sys

n = int(sys.stdin.readline())
result = []
for i in range(n):
    result.append(list(sys.stdin.readline().split()))
result.sort(key=lambda x: int(x[0]))
#print(result)
for i in range(len(result)):
    print(result[i][0], result[i][1])