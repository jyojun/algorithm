for i in range(1,20):
    for j in range(1, 20, 2):
        if j == 19:
            print(f'{i} * {j} = {i * j}')
        else:
            print(f'{i} * {j} = {i * j} / {i} * {j+1} = {i * (j+1)}')