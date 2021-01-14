import sys
input = sys.stdin.readline

N = int(input())
students = []
for i in range(N):
    w, h = map(int, input().split())
    students.append([w,h])

rank = []
for i in range(N):
    counts = 1
    for j in range(N):
        if i==j:
            continue
        else:
            if students[i][0] < students[j][0] and students[i][1] < students[j][1]:
                counts+=1
    rank.append(counts)
print(" ".join(str(i) for i in rank))