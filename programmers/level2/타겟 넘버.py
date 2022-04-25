cnt = 0

def dfs(i, total,order,numbers,target):
    global cnt

    if order == '+':
        total += numbers[i]
    else:
        total -= numbers[i]

    if i == len(numbers)-1:
        if total == target:
            cnt += 1
            return
        else:
            return

    dfs(i+1, total, '+', numbers, target)
    dfs(i+1, total, '-', numbers, target)

def solution(numbers, target):

    dfs(0, 0, '+', numbers, target)
    dfs(0, 0, '-', numbers, target)

    print(cnt)
    return cnt