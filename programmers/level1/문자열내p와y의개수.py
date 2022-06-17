def solution(s):
    pNum = 0
    yNum = 0

    for i in s:
        if i == 'p' or i == 'P':
            pNum += 1
        elif i == 'y' or i == 'Y':
            yNum += 1

    if pNum == yNum:
        return True
    else:
        return False
