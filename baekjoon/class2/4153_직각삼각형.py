import sys
input = sys.stdin.readline

a=b=c=1
while True:
    result = True
    a,b,c = map(int,input().split())
    num_list = [a,b,c]

    if a==0 and b==0 and c==0 :
        break
    max_num = max(num_list)

    result_sum = 0
    for i in num_list:
        #print(i)
        if i == max_num:
            continue
        result_sum += i**2
    
    if max_num**2 != result_sum:
        result = False

    if result:
        print('right')
    else:
        print('wrong')