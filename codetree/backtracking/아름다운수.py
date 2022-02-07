import sys

input = sys.stdin.readline

cnt = 0
num = []
n = int(input())

def is_beautiful():
    i = 0

    # n자리수 n번 반복
    while i<n:

        # i 번째에서 num[i] 에 해당하는 숫자가 n보다 크면 False
        if i + num[i] - 1 >= n:
            return False
        # i 번째에서 num[i] 에 해당하는 숫자크기만큼 연속해야하지 않으면 False
        for j in range(i, i + num[i]):
            if num[j] != num[i]:
                return False

        i += num[i]
    return True

def cnt_beautiful_num(x):
    global cnt

    if x == n:
        if is_beautiful():
            cnt += 1
        return
    
    for i in range(1, 5):
        num.append(i)
        cnt_beautiful_num(x+1)
        num.pop()

cnt_beautiful_num(0)
print(cnt)