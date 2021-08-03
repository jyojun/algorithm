N = int(input())
result = ['1', '11', '12']

for i in range(3,N):
    temp = result[i-1]
    num = ''
    count = 1
    for j in range(0,len(temp)-1):
        if temp[j] != temp[j+1]:
            num += temp[j] + str(count)
            count = 1
            if j == len(temp)-2:
                num += temp[j+1] + '1' # 마지막과 그 전이 다를 경우
        else:
            count += 1
            if j == len(temp)-2:
                num += temp[j+1] + str(count) # 마지막과 그 전이 같을 경우
    result.append(num)

print(result[N-1])