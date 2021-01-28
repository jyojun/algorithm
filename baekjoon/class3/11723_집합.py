import sys
input = sys.stdin.readline

def add_x(result, x):
    if not result[x]:
        result[x] = True

def remove_x(result, x):
    if result[x]:
        result[x] = False

def check_x(result, x):
    if result[x]:
        print(1)
    else:
        print(0)

def toggle_x(result, x):
    if result[x]:
        result[x] = False
    else:
        result[x] = True

def all_result(result):
    for i in range(1,20+1):
        result[i] = True

def clear_result(result):
    for i in range(1,20+1):
        result[i] = False

M = int(input())
result = [False] * 21
#print(result)

for i in range(M):
    opr = list(input().split())

    if opr[0] == 'add':
        add_x(result, int(opr[1]))
    elif opr[0] == 'remove':
        remove_x(result, int(opr[1]))
    elif opr[0] == 'check':
        check_x(result, int(opr[1]))
    elif opr[0] == 'toggle':
        toggle_x(result, int(opr[1]))
    elif opr[0] == 'all':
        all_result(result)
    else:
        clear_result(result)
    #print(result)