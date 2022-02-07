def solution(answers):
    answer = []
    p = [0,0,0]
    num1 = [1,2,3,4,5]
    num2 = [2,1,2,3,2,4,2,5]
    num3 = [3,3,1,1,2,2,4,4,5,5]
    for a in range(len(answers)):
        if num1[a % len(num1)] == answers[a]:
            p[0] += 1
        if num2[a % len(num2)] == answers[a]:
            p[1] += 1
        if num3[a % len(num3)] == answers[a]:
            p[2] += 1
    max_value = max(p)

    for i in range(3):
        if p[i] == max_value:
            answer.append(i+1)
    return answer