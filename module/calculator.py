def add(n1, n2):
    return n1 + n2


def sub(n1, n2):
    return n1 - n2


def mul(n1, n2):
    return n1 * n2


def div(n1, n2):
    if n2 != 0:
        return n1 / n2
    
    elif n2 == 0:
        return "모순 (분모는 0이 되면 안 됩니다.)"