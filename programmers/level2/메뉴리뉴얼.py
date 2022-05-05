from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    
    candidates = []
    for c in course:
        for order in orders:
            for com in combinations(order, c):
                li = ''.join(sorted(com))
                candidates.append(li)
    #print(Counter(candidates).most_common())
    
    visited = { c:0 for c in course }
    for i in Counter(candidates).most_common():
        if i[1] > 1 and visited[len(i[0])] <= i[1]:
            answer.append(i[0])
            visited[len(i[0])] = i[1]
            
    
        
    return sorted(answer)