def solution(sizes):
    max_w = 0
    max_h = 0

    for s in sizes:
        w, h = s
        if w < h:  # 가로가 세로보다 크다고 가정
            w, h = h, w
        if max_w < w:
            max_w = w
        if max_h < h:
            max_h = h
    return max_w * max_h
