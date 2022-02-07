import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int,input().split()))

result = 0

def xor_backtrack(curr_index, cnt, sum_val):
    global result

    if cnt == m:
        result = max(result, sum_val)
        return
    
    if curr_index == n:
        return
    
    # 선택하지 않은경우
    xor_backtrack(curr_index+1, cnt, sum_val)

    # 선택한 경우
    xor_backtrack(curr_index+1, cnt+1, sum_val ^ arr[curr_index])

xor_backtrack(0,0,0)

print(result)
