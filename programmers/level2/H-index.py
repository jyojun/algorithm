def solution(citations):
    citations = sorted(citations)
    maxh = 0
    for i in range(1, 10001):
        for j in range(len(citations)):
            if citations[j] >= i and len(citations)-j >= i:
                maxh = i
    return maxh
