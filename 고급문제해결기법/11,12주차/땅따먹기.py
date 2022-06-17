import sys

input = sys.stdin.readline

n, k = map(int, input().split())
boards = [list(map(int, input().split())) for _ in range(n)]
# print(boards)

visited = {(i, j): 0 for i in range(n) for j in range(n-2)}
checked = {(i, j): False for i in range(n) for j in range(n)}
# print(visited)
# print(checked)

dp = []
result = []
for i in range(len(boards)):
    curr_sum = sum(boards[i][:3])
    visited[(i, 0)] = curr_sum
    for j in range(3, n):
        curr_sum += boards[i][j] - boards[i][j-3]
        visited[(i, j-3+1)] = curr_sum
# print(visited)

for v in visited:
    i, j = v
    result.append([visited[v], i, j])
# print(result)

result.sort(key=lambda x: x[0], reverse=True)
# print(result)

answer = 0


def dfs(result, cnt, i, checked, total):
    global answer
    if i == len(result) and cnt != k:
        return
    if cnt == k:
        answer = max(answer, total)
        return
    x, y = result[i][1], result[i][2]
    if checked[(x, y)] == False and checked[(x, y+1)] == False and checked[(x, y+2)] == False:
        checked[(x, y)], checked[(x, y+1)
                                 ], checked[(x, y+1)] = True, True, True
        dfs(result, cnt+1, i+1, checked, total+result[i][0])

    dfs(result, cnt, i+1, checked, total)


for i in range(len(result)):
    dfs(result, 0, i, checked, 0)
# print(answer)
# print(checked)
# print(result)
x = n // 3
if x*n < k:
    print(-1)
else:
    print(answer)
