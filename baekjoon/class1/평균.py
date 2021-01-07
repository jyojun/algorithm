n = int(input())
score_list = list(map(int, input().split()))

M = max(score_list)
total = 0
for i in range(len(score_list)):
    total += score_list[i]/M*100

print(total/len(score_list))