def divide(p):
    open_p = 0
    close_p = 0
    
    for i in range(len(p)):
        if p[i] == '(':
            open_p += 1
        else:
            close_p += 1
        if open_p == close_p:
            return p[:i+1], p[i+1:]
        
def check(p):
    stack = []
    for x in p:
        if x == '(':
            stack.append(x)
        else:
            if not stack:
                return False
            stack.pop()
    return True


def solution(p):
    answer = ''
    
    # 빈 문자일 경우 빈 문자 반환
    if len(p) == 0:
        return ''
    
    # 문자열을 u,v로 나눔
    u, v = divide(p)
    
    # u가 올바른 괄호 문자열 이면 v에 대해 1단계를 수행
    if check(u):
        return u + solution(v)
    
    # u가 올바른 괄호 문자열이 아니면 4를 수행
    else:
        answer = '(' # 4-1
        answer += solution(v) # 4-2
        answer += ')' # 4-3
        
        for x in u[1:-1]: # 4-5 첫번째 마지막 문자열 제거한 문자열을 각각 반대로 붙임
            if x == '(':
                answer += ')'
            else:
                answer += '('

        return answer