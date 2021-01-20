import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())

dirts = [list(map(int, input().split())) for _ in range(N)]

min_time = 1000000000000
max_dirt = 0
for height in range(max(map(max, dirts))+1):

    diff1 = 0
    diff2 = 0
    for i in range(N):
        for j in range(M):
            if dirts[i][j] > height:
                diff1 += dirts[i][j]- height
            elif dirts[i][j] < height:
                diff2 += height-dirts[i][j]
            else:
                diff2 += height-dirts[i][j]

    dirt = diff1 - diff2
    total = dirt + B
    if total < 0:
        continue
    time = 2*diff1 + diff2
    if time <= min_time:
        min_time = time
        max_dirt = height
    #print(i,time, dirt+B)

print(min_time, max_dirt)