n = int(input())
result = []
for i in range(n):
    temp = int(input())
    result.append(temp)

result=sorted(result)
for i in result:
    print(i)