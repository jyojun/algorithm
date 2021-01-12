import sys
input = sys.stdin.readline
a=2
b=7
count=1
n = int(input())

if n==1:
    print(1)
else:
    while True:
        if a<=n and b>=n:
            break
        a+=6*count
        b+=6*(count+1)
        #print(a,b)
        count+=1
    print(count+1)