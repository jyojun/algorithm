'''
def bi_search_count(target, A):
    start = 0
    end = len(A) - 1
    count = 0
    while start <= end:
        mid = (start+end)//2

        if A[mid] == target:
            #print(A[start:end+1])
            count = A[start:end+1].count(target)
            return count
        elif A[mid] > target:
            end = mid-1
        else:
            start = mid+1
    return count
    
    if start>end:
        return 0
    else:
        mid = (start+end)//2

        if A[mid] == target:
            count += 1
        elif A[mid] > target:
            count += bi_search_count(start, mid-1, target, A, count)
        else:
            count += bi_search_count(mid+1, end, target, A, count)
    return count

'''
N = int(input())
A = sorted(list(map(int, input().split())))
M = int(input())
B = list(map(int, input().split()))
start = 0
end = len(A)-1
result = {}
for i in A:
    if(i in result):
        result[i] += 1
    else:
        result[i] = 1
#print(result)
str_result = ' '.join(str(result[x]) if x in result else '0' for x in B)
print(str_result)

#딕셔너리 방법으로 푼다. 
#이분탐색시 시간초과