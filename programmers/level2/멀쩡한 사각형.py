def gcd(x, y):
   # y가 0이 될 때까지 반복
    while y:
       # y를 x에 대입
       # x를 y로 나눈 나머지를 y에 대입
        x, y = y, x % y
    return x

def solution(w,h):
    x = w/gcd(w,h)
    y = h/gcd(w,h)
    result = (w*h)-((x+y-1)*gcd(w,h))
    return result