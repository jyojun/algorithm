import sys
input = sys.stdin.readline

n, q = map(int, input().split())
parents = {x: 0 for x in range(n+1)}  # 부모노드 값을 저장

for i in range(n-1):
    node1, node2 = map(int, input().split())
    parents[node2] = node1

# u가 v의 부모인지 확인하는 함수, 최악의 경우 트리 높이만큼 연산하므로, 시간복잡도 O(logN)


def isAncestor(u, v):
    while v >= 1:
        if u == v:
            return True
        v = parents[v]
    return False


cnt = 0
for i in range(q):
    u, v = map(int, input().split())
    if isAncestor(u, v):
        cnt += 1

print(cnt)

# 연산수 q만큼 isAncestor 함수를 불러오므로 q*logN 연산횟수 이므로 총 시간복잡도 O(q*logN) 이다.
