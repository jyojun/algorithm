import sys

input = sys.stdin.readline

N = int(input())

times = [list(map(int, input().split())) for _ in range(N)]
#print(times)
times = sorted(times, key=lambda x: x[0])
times = sorted(times, key=lambda x: x[1])
#print(times)

count = 1
max_start = times[0][1]
for i in range(1,len(times)):
    if times[i][0] >= max_start:
        max_start = times[i][1]
        count+=1
        #print(max_start)
print(count)