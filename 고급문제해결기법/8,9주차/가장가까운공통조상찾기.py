import sys
input = sys.stdin.readline

n, q = map(int, input().split())

graph = {x: [] for x in range(1, n+1)}  # graph를 구현할 딕셔너리
parents = {x: 0 for x in range(1, n+1)}  # 각각의 노드의 부모정보를 담을 딕셔너리

for i in range(n-1):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    parents[node2] = node1

depth = {x: 0 for x in range(1, n+1)}  # 각각의 깊이크기를 저장할 딕셔너리
depth[0] = 0
# depth 딕셔너리에 루트부터 리프노드까지 각각의 깊이 저장 -> 완전 탐색하므로 O(N)


def find_depth(x, curr_dep):
    depth[x] = curr_dep
    for i in graph[x]:
        find_depth(i, curr_dep+1)
    return


find_depth(1, 1)

# 깊이만큼 반복하므로, 최대 logN 만큼 반복 -> O(logN)


def find_LCA(u, v):
    u_dep = depth[u]  # u,v 각각의 depth 크기를 변수에 저장
    v_dep = depth[v]
    if u_dep > v_dep:  # u의 깊이가 더 깊다면 v와 같아질 때까지 u에 부모노드를 저장
        for i in range(u_dep-v_dep):
            u = parents[u]
    elif u_dep < v_dep:  # v의 깊이가 더 깊다면 u와 같아질 때까지 v에 부모노드를 저장
        for i in range(v_dep-u_dep):
            v = parents[v]

    if u == v:  # 깊이를 갖게 만든 후 둘이 같다면 한쪽을 출력
        return u
    else:  # 깊이가 갖지만 둘이 다르다면 같아질 때 까지 부모노드로 올라간 후 출력 (적어도 루트노드에서 같아짐)
        while u != v:
            u, v = parents[u], parents[v]
    return u


# q의 갯수 만큼 반복하므로 질의수(q) * find_LCA (logN) + find_depth(N) 연산횟수이므로 전체 시간복잡도 : O(q*logN + N)
for i in range(q):
    u, v = map(int, input().split())
    print(find_LCA(u, v))
