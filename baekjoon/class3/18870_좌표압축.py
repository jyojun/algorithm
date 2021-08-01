import sys

input = sys.stdin.readline

N = int(input())

result = [0] * N

x = list(map(int, input().split()))

h = []

for i in range(N):
    h.append([i, x[i]])
h = sorted(h, key=lambda x: x[1])

print(h)
count = 0
compare = 0

if h[N-1][1] > h[N-2][1]:
    compare = 1
for i in range(0,N-1):
    print(count)
    h[i][1] = count
    if h[i+1][1] > h[i][1]:
        count+=1
        print(True)
    print(i)

print(h)

for i in range(N):
    result[h[i][0]] = h[i][1]

print(result)