def solution(N, number):
    answer = -1
    dp = []

    for i in range(1, 9):  # 최소값이 8보다 크면 -1 출력이므로 9까지 구한다.
        all_case = set()
        first_case = int(str(N) * i)  # 모든 dp의 첫번째는 N, NN, NNN, NNNN 이다.
        all_case.add(first_case)
        # ex) dp[3] = dp[1], dp[2] 의 모든 사칙연산, dp[2], dp[1]의 모든 사칙연산
        for j in range(i-1):
            for op1 in dp[j]:
                for op2 in dp[-j-1]:
                    all_case.add(op1 + op2)
                    all_case.add(op1 - op2)
                    all_case.add(op1 * op2)
                    if op2 != 0:
                        all_case.add(op1 / op2)

        if number in all_case:
            answer = i
            break

        dp.append(all_case)

    return answer
