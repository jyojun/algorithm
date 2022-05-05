import collections


def solution(str1, str2):
    answer = 0

    # 대문자로 모두 변경
    str1 = str1.upper()
    str2 = str2.upper()

    list1 = [str1[x]+str1[x+1]
             for x in range(len(str1)-1) if str1[x].isalpha() and str1[x+1].isalpha()]
    list2 = [str2[x]+str2[x+1]
             for x in range(len(str2)-1) if str2[x].isalpha() and str2[x+1].isalpha()]

    list1 = collections.Counter(list1)
    list2 = collections.Counter(list2)

    gyo = {}
    hap = {}

    # 교집합
    for x in list1:
        for y in list2:
            if x == y:
                gyo[x] = min(list1[x], list2[y])

    gyo = collections.Counter(gyo)

    # 합집합 => list1+list2-교집합
    hap = (list1+list2-gyo)

    num1 = 0
    num2 = 0

    for i in gyo:
        num1 += gyo[i]
    for i in hap:
        num2 += hap[i]

    if num1 == 0 and num2 == 0:
        return 65536

    return int((num1/num2) * 65536)
