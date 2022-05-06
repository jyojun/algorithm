import itertools


def calc(op, seq, exp):
    if exp.isdigit():
        return str(exp)
    else:
        if op[seq] == "*":
            split_data = exp.split('*')  # 연산자를 *로 쪼갬
            temp = []
            for s in split_data:
                temp.append(calc(op, seq+1, s))
            return str(eval("*".join(temp)))
        elif op[seq] == '+':
            split_data = exp.split('+')
            temp = []
            for s in split_data:
                temp.append(calc(op, seq+1, s))
            return str(eval('+'.join(temp)))
        else:
            split_data = exp.split('-')
            temp = []
            for s in split_data:
                temp.append(calc(op, seq+1, s))
            return str(eval('-'.join(temp)))


def solution(expression):
    answer = 0

    order = ['+', '-', '*']
    order = itertools.permutations(order, 3)

    result = []
    for o in order:
        result.append(abs(int(calc(o, 0, expression))))
    print(result)

    return max(result)
