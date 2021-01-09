n = int(input())
result = [] 
for i in range(n):
    x,y = map(int, input().split())
    result.append([x,y])
result = sorted(result)
for i in range(len(result)):
    print(result[i][0], result[i][1])