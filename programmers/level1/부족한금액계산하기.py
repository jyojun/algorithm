def solution(price, money, count):
    fee = ((count * (count+1)) / 2) * price

    if money > fee:  # 모자라지 않을경우 0을 리턴
        return 0
    else:
        return fee - money
