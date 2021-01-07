n, m = map(int, input().split())
card_list = list(map(int, input().split()))

result = []

def sum_card_list(card_list):
    global result
    for i in range(len(card_list)):
        for j in range(i+1, len(card_list)):
            for k in range(j+1, len(card_list)):
                result.append(card_list[i]+card_list[j]+card_list[k])

sum_card_list(card_list)
max = 0
for i in result:
    if i > max and i <= m:
        max = i
print(max)