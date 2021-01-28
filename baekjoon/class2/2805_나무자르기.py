import sys
input = sys.stdin.readline

N, M = map(int, input().split())

woods = list(map(int, input().split()))

start, end = 1, max(woods)

result = 0
while start <= end:
    mid = (start+end)//2
    sum_woods = 0
    sum_woods = sum([wood-mid for wood in woods if wood>mid])

    if sum_woods < M: # 별로 안잘렸으면,
        end = mid-1 #높이를 더 낮게 지정해야한다.
        #print(sum_woods,mid, 1)

    else: #M보다 많이 자르거나, M과 같다면
        start = mid+1 #높이를 높게 설정해줘도 된다. 
        #print(sum_woods, mid, 2)
        result = mid

print(result)