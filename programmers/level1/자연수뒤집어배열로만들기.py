def solution(n):
    answer = []

    temp = str(n)
    for i in temp[-1::-1]:
        answer.append(int(i))
    return answer
