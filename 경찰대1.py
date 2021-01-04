L = int(input())
R = int(input())

length = 6
total_length = 0
count = 1
while True:
    count *= 2
    length = L * (R/100)
    #print(length)
    length = int(length)
    if(length<=5):
        break
    total_length += count*length
    L = length

print(total_length)