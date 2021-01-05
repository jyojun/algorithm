n = int(input())
list_num = list(map(int, input().split()))

max_num = -1000000
min_num = 1000000 

for i in list_num:
    if max_num < i:
        max_num = i
    if min_num > i:
        min_num = i

print(min_num, max_num)