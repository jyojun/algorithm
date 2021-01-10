def bi_search_count(target, A):
    count = 0
    start = 0
    end = len(A)-1

    while start <= end:
        mid = (start+end)//2

        if A[mid] == target:
            count = A.count(target)
            return count
        elif A[mid] > target:
            end = mid-1
        else:
            start = mid+1
    return count

N = int(input())
A = sorted(list(map(int, input().split())))
M = int(input())
B = list(map(int, input().split()))

result = []
for i in range(M):
    result.append(bi_search_count(B[i], A))

str_result = ' '.join(str(result[x]) for x in range(M))
print(str_result)