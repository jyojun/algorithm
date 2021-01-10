import math

n= int(input())
A = list(map(int, input().split()))

def is_prime(n):
    if n==2:
        return True
    elif n==0 or n==1:
        return False
    else:
        if n%2 == 0:
            return False
        #root_n = math.sqrt(n)
        for i in range(3, n):
            if n%i==0:
                return False
        return True
count = 0
for i in A:
    if is_prime(i):
        count+=1

print(count)