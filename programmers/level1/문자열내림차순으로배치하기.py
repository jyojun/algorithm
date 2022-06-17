def solution(s):
    s = list(s)
    s.sort(reverse=True)
    s = "".join(s)
    return s
