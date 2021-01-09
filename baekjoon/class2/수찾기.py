def bi_search(target, A):
    start = 0
    end = len(A)-1

    while start <= end:
        mid = (start+end)//2

        if A[mid] == target:
            return 1
        elif A[mid] < target:
            start = mid+1
        else:
            end = mid-1
    return 0
N = int(input())
A = list(map(int, input().split()))
A.sort()
M = int(input())
B = list(map(int, input().split()))

#print(A, B)
for i in B:
    print(bi_search(i, A))