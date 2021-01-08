n = int(input())
words = []
for i in range(n):
    word = input()
    if word in words:
        continue
    words.append(word)
result = []
for i in range(51):
    result.append([])
#print(result)
words = sorted(words)

for i in words:
    result[len(i)].append(i)
#print(result)
for i in range(len(result)):
    if len(result[i]) == 0:
        continue
    else:
        result[i] = sorted(result[i])
#print(result)
for i in range(len(result)):
    if len(result[i]) == 0:
        continue
    else:
        for j in result[i]:
            print(j)