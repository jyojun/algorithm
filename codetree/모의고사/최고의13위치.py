import sys

input = sys.stdin.readline

N = int(input())

grid = [ 
    list(map(int,input().split()))
    for _ in range(N)
]

result = []


def in_range(x, y):
    return 0 <= x and x < N and 0 <= y and y < N

def cnt13(x, y):
    
    cnt = 0

    for i in range(3):
        if in_range(x, y+i):
            cnt += grid[x][y+i]
        else:
            return -1

    return cnt

for i in range(N):
    for j in range(N):
        for r in range(N):
            for c in range(N):
                if ([i,j] != [r, c]) and ([i,j] != [r, c-1]) and ([i,j] != [r, c-2]):
                    if ([r,c] != [i, j]) and ([r,c] != [i, j-1]) and ([r,c] != [i, j-2]):
                            
                        cnt = 0
                        if cnt13(i,j) != -1 and cnt13(r,c) != -1:
                            cnt += cnt13(i,j) + cnt13(r,c)
                            result.append(cnt)
                            #print(i,j, r,c)
                        else:
                            continue
                else:
                    continue

print(max(result))
        