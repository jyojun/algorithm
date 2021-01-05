def solution(n):
    answer = ''
    temp = n
    while(temp):
        a = temp%3
        if a == 0:
            a = 4
            temp = int(temp/3) - 1
        else:
            temp = int(temp/3)
        answer += str(a)
    return answer[::-1]