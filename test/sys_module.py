import sys


print(sys.argv)

def add(n1, n2):
    return n1 + n2


if len(sys.argv) == 3:
    print(add(int(sys.argv[1]), int(sys.argv[2])))
    
else:
    print("사용법 : python _FileName_ 임의의 양의 자연수 두 개")