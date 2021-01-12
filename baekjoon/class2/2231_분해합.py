import sys
input = sys.stdin.readline

n = int(input())
result = []
count = 0
for i in range(1,n):
    temp = str(i)
    sum_temp = 0

    for j in range(len(temp)):
        sum_temp += ord(temp[j])-48 # 'a'의 아스키코드 값보다 1적은 값을 빼줌.
    sum_temp += int(temp)

    if sum_temp == n:
        result.append(i)
        count +=1
if count==0:
    print(0)
else:
    print(min(result))