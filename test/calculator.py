def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def multi(n1, n2):
    return n1 * n2


def div(n1, n2):
    if n2 != 0:
        return n1 / n2
    
    elif n2 == 0:
        return "모순 : 0으로 나눌 수 없습니다."