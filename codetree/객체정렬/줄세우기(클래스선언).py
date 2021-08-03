import sys

input = sys.stdin.readline

# 클래스 선언
class Student:
    def __init__(self, height, weight, number):
        self.height, self.weight, self.number = height, weight, number
    
# 변수 선언 및 입력
n = int(input())
given_inputs = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

students = [
    Student(height, weight, i+1) # 학생 순서대로 생성 (번호는 + 1)
    for i, (height, weight) in enumberate(given_inputs)
]

# Custom Comparator를 활용한 정렬
students.sort(key = lambda x: (-x.height, -x.weight, x.number))

# 출력
for student in students:
    print(student.height, student.weight, student.number)