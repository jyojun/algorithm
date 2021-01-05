num_list = [int(input()) for i in range(3)]
result = num_list[0]*num_list[1]*num_list[2]
result = str(result)

for i in range(10):
    print(result.count(str(i)))