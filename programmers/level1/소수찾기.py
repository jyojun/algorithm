import math


def solution(n):
    is_prime = [True] * (n+1)

    for i in range(2, int(math.sqrt(n))+1):
        if is_prime[i] == True:
            j = 2
            while i * j <= n:
                is_prime[i*j] = False
                j += 1

    return len([x for x in is_prime if x == True]) - 2
