import sys

input = sys.stdin.readline

N, M = map(int, input().split())

memo = dict()

for i in range(N):
    site, pw = map(str, input().split())

    memo[site] = pw

#print(memo)

for i in range(M):
    input_site = input()
    input_site = input_site.replace('\n', "")
    print(memo[input_site])