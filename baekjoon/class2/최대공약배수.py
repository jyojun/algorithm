a,b = map(int, input().split())

def division(x,y):
    while True:
        a = x%y
        x = y
        y = a
        if a==0:
            return x

def multiple(x,y):
    a=x//division(x,y)
    b=y//division(x,y)
    return a*b*division(x,y)

print(division(a,b))
print(multiple(a,b))