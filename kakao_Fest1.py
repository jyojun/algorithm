st11 = 1
st12 = st11+2
st13 = st12+3
st14 = st13+4
st15 = st14+5
st16 = st15+6

st21 = 1
st22 = st21+2
st23 = st22+4
st24 = st23+8
st25 = st24+16

def result1(n):
    if n == st11: return 5000000
    elif n<= st12 and n>st11: return 3000000
    elif n<= st13 and n>st12: return 2000000
    elif n<= st14 and n>st13: return 500000
    elif n<= st15 and n>st14: return 300000
    elif n<= st16 and n>st15: return 100000
    else: return 0

def result2(n):
    if n == st21: return 5120000
    elif n<= st22 and n>st21: return 2560000
    elif n<= st23 and n>st22: return 1280000
    elif n<= st24 and n>st23: return 640000
    elif n<= st25 and n>st24: return 320000
    else: return 0

n = int(input())

for i in range(n):
    a, b = map(int, input().split())
    print(result1(a) + result2(b))



