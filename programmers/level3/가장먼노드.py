from collections import deque


def solution(n, edge):
    max_dist = 0
    graph = {i: [] for i in range(1, n+1)}

    for e in edge:
        x, y = e
        if not y in graph[x]:
            graph[x].append(y)
        if not x in graph[y]:
            graph[y].append(x)

    distance = {i: 0 for i in range(1, n+1)}
    visited = [False] * (n+1)

    def bfs(x):
        max_dist = 0
        q = deque()
        q.append(x)
        visited[x] = True
        while q:
            g = q.popleft()
            for w in graph[g]:
                if not visited[w]:
                    visited[w] = True
                    distance[w] = distance[g] + 1
                    q.append(w)
                    if max_dist < distance[w]:
                        max_dist = distance[w]
        return max_dist
    max_dist = bfs(1)

    cnt = 0

    for d in distance:
        if distance[d] == max_dist:
            cnt += 1

    return cnt
