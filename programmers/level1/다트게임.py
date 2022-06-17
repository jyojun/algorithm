def solution(dartResult):
    points = []

    if not(dartResult[-1] == '*' or dartResult[-1] == '#'):
        dartResult += '?'
    num = ''
    for i in range(len(dartResult)):
        if dartResult[i].isdigit():
            num += dartResult[i]
        else:
            if dartResult[i] >= 'A' and dartResult[i] <= 'Z':
                if dartResult[i] == 'D':
                    points.append(int(num)**2)

                elif dartResult[i] == 'T':
                    points.append(int(num)**3)

                else:
                    points.append(int(num))
                num = ""

            if dartResult[i] == "*":
                if len(points) == 1:
                    points[-1] *= 2
                else:
                    points[-1] *= 2
                    points[-1-1] *= 2
            elif dartResult[i] == '#':
                points[-1] *= -1
    return sum(points)
