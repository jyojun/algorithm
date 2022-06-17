def solve(a, b, t):
    # 코드 + 출력
    start = t // a
    result = []
    chickens = []

    # 후라이드 먹을 수 있는 시간으로 나누었을 때 몫 갯수부터 시작
    while start >= 0:
        temp = t - (start * a)

        # 나머지를 모두 저장 !
        result.append([temp % b, start+(temp//b)])

        # t시간에 딱 맞추어 먹을 수 있을 경우
        if temp % b == 0:

            # t시간에 먹을 수 있을 때, 후라이드 + 양념 치킨수를 더한값을 저장
            chickens.append(start + temp//b)
        start -= 1

    # t시간에 딱 맞추어 먹을 수 있는 치킨 수를 저장한 리스트에 원소가 있으면 chickens중 최댓값을 출력
    if chickens:
        print(max(chickens))

    # t시간에 딱 맞추어 먹을 수 없다면 치킨을 먹고 나머지시간이 가장 작은 값을 출력
    else:
        answer = min(result)
        print(answer[1], answer[0])


a, b, t = [int(x) for x in input().split()]
solve(a, b, t)

# 시간복잡도는 t를 a로 나눈 크기만큼 반복하므로, O(t//a) 이다.
