def solve(a,b,c):

    '''
    while(reach != c):
        day += 1
        reach += a
        if(reach >= c):
            break
        reach -= b
        #print(day)
    return day
    '''

    temp = c-a-1

    result = temp//(a-b) + 2
    
    return result
a, b, c = map(int, input().split(" "))

print(solve(a,b,c))