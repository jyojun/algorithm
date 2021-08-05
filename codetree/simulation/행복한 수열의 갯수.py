import sys

input = sys.stdin.readline

n, m = map(int, input().split())

arr = [ list(map(int, input().split())) for _ in range(n) ]
result_cnt = 0

for i in range(n):
    cnt, max_cnt = 1, 1
    # 가로로
    for j in range(1, n):
        if arr[i][j-1] == arr[i][j]:
            cnt += 1

            if max_cnt < cnt:
                max_cnt = cnt

            if max_cnt >= m:
                result_cnt += 1
                break
        else:
            cnt = 1
            if max_cnt >= m:
                result_cnt += 1
                break

for i in range(n):    
    cnt, max_cnt = 1, 1
    # 세로로
    for j in range(1, n):
        if arr[j-1][i] == arr[j][i]:
            cnt += 1
            
            if max_cnt < cnt:
                max_cnt = cnt
            
            if max_cnt >= m:
                result_cnt += 1
                break
        else:
            cnt = 1
            if cnt >= m:
                result_cnt += 1
                break

print(result_cnt)    
    