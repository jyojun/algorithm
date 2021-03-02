import sys

input = sys.stdin.readline

N = int(input())

people = list(map(int, input().split()))

people.sort()

sum = 0
temp = 0

for i in range(len(people)):
    temp += people[i]
    sum += temp
print(sum)