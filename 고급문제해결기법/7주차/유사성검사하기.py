import sys
import bisect
input = sys.stdin.readline

n = int(input())
P = list(map(int, input().split()))
Q = list(map(int, input().split()))

PnQ = [[p, q] for p, q in zip(P, Q)]

# P값이 셋중 둘이라도 같은 경우 Q[i] < Q[j] < Q[k]경우가 나오지 않게 하기 위해 P값이 같은 경우 Q값을 반대로 정렬한다.
# O(NlogN)
PnQ = sorted(PnQ, key=lambda x: (x[0], -x[1]))

# Q를 따로 생성한 후 PnQ에 P의 오름차순으로 정렬한 순서대로 Q에 Q값을 저장 O(N)
Q = []
for pnq in PnQ:
    Q.append(pnq[1])

# Binary Indexed Tree update 함수 O(logN)


def update(BIT, n, i, value):
    while i <= n:
        BIT[i] += value
        i += (i & -i)

# Binary Indexed Tree 구간 합을 구하기 위한 query 함수 O(logN)


def query(BIT, i):
    summ = 0
    while i > 0:
        summ += BIT[i]
        i -= (i & -i)

    return summ


def getCount(arr, n):

    # 좌표 압축을 하고 인덱스를 모두 1씩 증가 (Binary Indexed Tree를 사용하기 위해 인덱스1~n을 사용하기 때문)
    xt = list(sorted(set(arr)))
    xt = {xt[i]: i for i in range(len(xt))}
    arr = ([xt[i]+1 for i in arr])

    BIT = [0] * (n+1)
    smaller_left = [0] * (n+1)
    bigger_right = [0] * (n+1)

    # 현재 탐색하는 원소의 왼쪽에서 더 작은 값을 세는 경우
    # 왼쪽부터 탐색하여 1부터 트리보다 작은 수(arr[i]-1)의 갯수를 구한다.
    # 업데이트 할때는 현재 탐색중인 값의 갯수를 1개씩 늘리기 위해 그 값의 트리 index자리에 업데이트한다.
    # O(NlogN)
    for i in range(n):
        smaller_left[i] = query(BIT, arr[i]-1)  # arr[i]-1 까지 등장한 횟수의 합
        update(BIT, n, arr[i], 1)

    for i in range(n+1):
        BIT[i] = 0

    # 현재 탐색하는 원소의 오른쪽에서 더 큰 값을 세는 경우
    # 오른쪽 부터 왼쪽으로 탐색하여 (현재 오른쪽에 있는 갯수 - 1부터 현재 값까지 갯수)를 구한다.
    # 업데이트를 할때 트리의 인덱스 현재값위치에 1을 추가 업데이트 해준다.
    # O(NlogN)
    for i in range(n-1, -1, -1):
        bigger_right[i] = (n-1-i) - query(BIT, arr[i])  # (n-1-i) - arr[i]까지의 합
        update(BIT, n, arr[i], 1)
        # print(BIT)
        #print("bigger_right",i, bigger_right[i])

    ans = 0

    for i in range(n):
        ans += smaller_left[i] * bigger_right[i]
        #print(smaller_left[i], bigger_right[i])
        #print("ans:", ans)

    return ans


print(getCount(Q, n))

# P는 현재 오름차순 되어 있으므로 Q의 값에서 탐색 할 때, 현재 값보다 왼쪽 인덱스에서 더 작고, 현재 값보다 오른쪽 인덱스에 있는 값에서 더 큰 값의 갯수를
# 각각 곱해주면 Q[i] < Q[j] < Q[k]을 만족하는 순서쌍의 갯수를 구할 수 있다.

# 위 getCount 함수의 시간복잡도는 n만큼 반복하여 O(logn) 시간복잡도를 갖는 update, query 해주므로 O(NlogN)을 갖고
# 처음 정렬하는 시간도 O(NlogN)의 시간복잡도를 갖는다.
# 따라서 총 O(NlogN)의 시간복잡도를 갖는다.
