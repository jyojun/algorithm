import sys

input = sys.stdin.readline

zenga = []

n = int(input())

for i in range(n):
    temp = int(input())
    zenga.append(temp)

s1, e1 = map(int, input().split())
s2, e2 = map(int, input().split())

s1, e1, s2, e2 = s1-1, e1-1, s2-1, e2-1

zenga = zenga[:s1] + zenga[e1+1:]
zenga = zenga[:s2] + zenga[e2+1:]

print(len(zenga))

for i in range(len(zenga)):
    print(zenga[i])