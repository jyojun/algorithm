import sys

input = sys.stdin.readline

C = int(input())
students = []
for i in range(C):
    students = list(map(int, input().split()))
    N = students[0]

    average = sum(students[1:]) / N
    count = 0
    for student in students[1:]:
        if(student > average):
            count+=1
    
    print('{:.3f}%'.format(round(count/N*100, 3)))