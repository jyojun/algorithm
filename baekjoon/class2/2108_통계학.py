import sys
from collections import Counter

input = sys.stdin.readline

N = int(input())
result = []
for i in range(N):
    result.append(int(input()))

result = sorted(result)
#print(result)
print(round(sum(result)/len(result))) #산술평균
print(result[len(result)//2]) #중간값

#print(Counter(result).most_common())

frequency = Counter(result).most_common()

if len(result) > 1:
    if frequency[0][1] == frequency[1][1]:
        print(frequency[1][0]) #최빈값
    else:
        print(frequency[0][0])
else:
    print(result[0])
print(result[len(result)-1]-result[0]) #범위