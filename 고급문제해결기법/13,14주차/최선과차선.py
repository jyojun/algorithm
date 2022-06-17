import heapq
import sys

input = sys.stdin.readline

INF = 1e8

n = int(input())  # 노드수
m = int(input())  # 엣지수
graph = [[] for _ in range(n)]

# 입력받은 간선수만큼 그래프 리스트에 저장, 시간복잡도 O(m)
for _ in range(m):
    u, v, w = map(int, input().split())  # u: 출발노드, v: 도착노드, w: 연결된 간선의 가중치
    graph[u].append((v, w))  # 출발노드의 도착노드정보와 가중치를 같이 입력

# print(graph)

# 그래프 노드 수 만큼 최선, 차선 경로를 저장할 distance 리스트 생성, 시간복잡도 O(n)
distance = [[INF]*2 for _ in range(n)]


def dijkstra(start):
    q = []

    # heapq를 사용하여 경로가 짧은 순서대로오게 push 한다. 시간복잡도 O(logm)
    heapq.heappush(q, (0, start))  # 우선순위, 값 형태로 들어간다.
    distance[start][0] = 0

    # q리스트에는 간선수만큼 push되고 pop되니 간선의 수만큼 반복하게 된다
    while q:
        dist, node = heapq.heappop(q)

        # 인접한 정점을 검사 하고, q를 업데이트 해야함. 시간복잡도 O(mlogm)
        for n, d in graph[node]:
            new_dist = dist+d
            if n != start and new_dist <= distance[n][1]:
                distance[n][1] = new_dist
                distance[n].sort()  # 2개이므로 이부분은 무시할 수 있다.(2log2)
                heapq.heappush(q, (new_dist, n))


dijkstra(0)
# print(distance)
result = 0
for i in range(1, n):
    if distance[i][1] != INF:
        result += distance[i][1]
print(result)

# 다익스트라 과정에서 distance의 각 원소를 최선의 경로만 구하는 숫자에서 최선과, 차선을 모두 저장하는 리스트로 바꿔주기만 했다.
# 공간복잡도는 기존 최선만 구하는 다익스트라보다 더 높게 요구되기는 한다.
# 위 과정을 모두 더하면 O(n + m + mlogm) 인데 m은 mlogm에 의해 무시할 수 있으므로
# 다익스트라 시간복잡도와 같은 O(n + mlogm) 이다.  간선의 갯수 m는 노드의 갯수 n^2보다는 작으므로, logm = logn과 동일하다고 볼 수 도있다.
