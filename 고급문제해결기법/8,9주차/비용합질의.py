import sys
input = sys.stdin.readline

n, q = map(int, input().split())

costs = list(map(int, input().split()))
costs.insert(0, 0)

graph = {x: [] for x in range(1, n+1)}
parents = {x: 0 for x in range(1, n+1)}  # 자신의 부모노드값을 저장

for i in range(n-1):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    parents[node2] = node1


# preorder 하였을 때, 자신의 각 자식노드들의 비용 누적합을 저장.
graph_cost = {x: 0 for x in range(1, n+1)}

# preorder bfs 형식으로 구현했기 때문에 모든 노드를 방문하므로, O(N) 시간이 소요된다.


def preorder_cost(x):
    cost = costs[x]
    for i in graph[x]:
        cost += preorder_cost(i)
        parents[i] = x
    graph_cost[x] = cost
    return cost

# 부모노트로 올라가면서, 현재노드가 변경되면, 루트 노트까지 update 해준다.
# 최악의 경우에는 트리 높이만큼 연산하므로, O(logN) 시간복잡도가 소요된다.


def update(v, d):
    i = v
    while i != 0:
        graph_cost[i] += d
        i = parents[i]


# query는 자식노드까지 누적합을 출력하면 되므로 시간복잡도 O(1)
def query(v):
    return graph_cost[v]


# 루트노드부터 순회 O(N)
preorder_cost(1)

for i in range(q):
    order = input().split()
    if(order[0] == 'subtree'):
        v = int(order[1])
        print(query(v))
    else:
        v, d = int(order[1]), int(order[2])
        update(v, d)

# 질의수 q번만큼 query, update를 하기 때문에 q * (1 + logN) 이므로 총 시간복잡도 : O(q*logN)
