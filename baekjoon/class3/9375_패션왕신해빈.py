import sys

input = sys.stdin.readline

T = int(input())

for i in range(T):
    N = int(input())
    clothes_list = {}
    for j in range(N):
        clothes = input().split(' ')
        clothes_name = clothes[0]
        clothes_sort = clothes[1].replace('\n', '')
        
        if clothes_sort in clothes_list:
            clothes_list[clothes_sort].append(clothes_name)
        else:
            clothes_list[clothes_sort] = [clothes_name]
        #print(clothes_list)
    result = 1
    for j in clothes_list:
        result *= (len(clothes_list[j])+1)
        #print(result)
    print(result-1)