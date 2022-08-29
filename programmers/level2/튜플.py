def solution(s):
    answer = []
    numbers = {i: 0 for i in range(1, 100001)}

    s = s.replace("}", "")
    s = s.replace("{", "")
    s = s.split(",")

    for x in s:
        numbers[int(x)] += 1

    result = []
    for n in numbers:
        if numbers[n] > 0:
            result.append((n, numbers[n]))

    result.sort(key=lambda x: (-x[1]))
    print(result)

    for i in result:
        answer.append(i[0])
    return answer
