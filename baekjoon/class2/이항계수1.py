n, k = map(int, input().split())
n2 = k2 = 1
for i in range(k):
    n2 *= n
    n -= 1
    k2 *= k
    k -= 1
print(int(n2/k2))