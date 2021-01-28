import sys
input = sys.stdin.readline

K, N = map(int, input().split())

lines = [int(input()) for _ in range(K)] 

start, end = 1, max(lines)
result = 0
while start <= end:
    mid = (start+end)//2

    cut_sum = sum([line//mid for line in lines])
    #print(cut_sum)

    if cut_sum >= N: # 자른 랜선의 갯수가 N보다 크거나 같을 경우
        start = mid+1 # 자를 랜선의 기준을 더 크게 잡아서 랜선의 갯수를 줄여줌
        result = mid #가장 마지막에 나온 mid 값이 정답
    else: #자른 랜선의 갯수가 N보다 작을 경우
        end = mid-1 # 더 작게 잡아서 랜선의 갯수를 늘려줌

print(result)