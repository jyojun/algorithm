import sys
input = sys.stdin.readline  
'''
n = int(input())
result = []
#print(result)
for i in range(n):
    temp = int(input())
    result.append(temp)

result = sorted(result)

for i in range(n):
    print(result[i])
'''
n = int(input())

result = [0 for i in range(10001)]

for i in range(n):
    result[int(input())] += 1

for i in range(len(result)):
    if result[i] != 0:
        for j in range(result[i]):
            print(i)