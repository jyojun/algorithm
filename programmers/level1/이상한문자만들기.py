def solution(s):
    answer = ""
    idx = 0
    for i in s:
        if i == " ":
            idx = 0
            answer += i
            continue
        if idx % 2 == 0:
            answer += i.upper()
        else:
            answer += i.lower()
        idx += 1

    return answer
