def solution(numbers):
    numbers = [str(i) for i in numbers]
    numbers = sorted(numbers, key=lambda x: x*3,
                     reverse=True)  # number의 크기는 1000 이하이므로
    return str(int("".join(numbers)))
