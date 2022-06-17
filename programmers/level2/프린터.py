from collections import deque


def solution(priorities, location):
    cnt = 0
    p = deque([[priorities[i], i] for i in range(len(priorities))])
    # print(p)
    while p:
        current = p.popleft()
        isExist = False
        for i in range(len(p)):
            if current[0] < p[i][0]:
                isExist = True

        # 더 중요한 문서가 있으면
        if isExist:
            p.append(current)
        else:
            cnt += 1
            if current[1] == location:
                break
    return cnt
