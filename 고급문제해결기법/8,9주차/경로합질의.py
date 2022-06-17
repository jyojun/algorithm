import sys
input = sys.stdin.readline

n, q = map(int, input().split())

costs = list(map(int, input().split()))
costs.insert(0, 0)

graph = {x: [] for x in range(1, n+1)}  # 각 노드의 자식노드값을 저장
parents = {x: 0 for x in range(1, n+1)}  # 자신의 부모노드값을 저장

for i in range(n-1):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    parents[node2] = node1

# update 함수는 v의 비용만 d만큼 더해주는 것 뿐이라 O(1)


def update(v, d):  # 업데이트 함수는 v 비용을 d만큼 더한다
    costs[v] += d

# query함수는 현재노드에서 루트노트까지 연산하는 것이니 최악의 경우라도 logN번의 연산 이라 O(logN)


def query(v):  # query함수는 조상 노드로 올라가면서 노드까지의 cost까지 더해준다.
    cost = 0
    i = v
    while i != 0:  # 루트노드까지 반복
        cost += costs[i]  # 부모노드롤 저장하면서 cost를 더해줌
        i = parents[i]
        #print("cost", cost, i)
    return cost


for i in range(q):
    order = input().split()
    if(order[0] == 'sum'):
        v = int(order[1])
        print(query(v))
    else:
        v, d = int(order[1]), int(order[2])
        update(v, d)

# 연산의 수 q 만큼 query, update를 반복하는 것이니, 총 O(q*logN) 시간 복잡도가 사용된다.
