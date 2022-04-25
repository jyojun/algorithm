def solution(n):
    three = ''
    
    while n != 0:
        three += str(n % 3)
        n = n // 3
    
    three = list(three)
    
    #print(three)
    
    result = 0
    for i in range(len(three)):
        result += int(three[i])*(3**(len(three)-1-i))
    return result