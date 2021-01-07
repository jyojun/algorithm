x,y,w,h = map(int, input().split())
if w-x < x:
    a = w-x
else:
    a = x
if h-y < y:
    b = h-y
else:
    b = y

if a<b:
    print(a)
else:
    print(b)