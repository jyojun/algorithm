def solution(rows, columns, queries):
    answer = []
    
    graph = [ [] for x in range(rows) ]
    
    for i in range(rows):
        for j in range(1,columns+1):
            graph[i].append(j+(i*columns))
            
    print(graph)
        
    for query in queries:
        min_value = []
        x1, y1, x2, y2 = query
        x1, y1, x2, y2 = x1-1, y1-1, x2-1, y2-1
        
        temp = graph[x1][y1]
        
        for i in range(x1, x2):
            min_value.append(graph[i][y1])
            graph[i][y1] = graph[i+1][y1]
        for i in range(y1, y2):
            min_value.append(graph[x2][i])
            graph[x2][i] = graph[x2][i+1]
        for i in range(x2, x1, -1):
            min_value.append(graph[i][y2])
            graph[i][y2] = graph[i-1][y2]
        for i in range(y2, y1, -1):
            min_value.append(graph[x1][i])
            graph[x1][i] = graph[x1][i-1]
            
        graph[x1][y1+1] = temp
        answer.append(min(min_value))
    return answer