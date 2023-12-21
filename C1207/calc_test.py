from calc import *
from sys import argv


if len(argv) == 3:
    print(add(int(argv[1]), int(argv[2])))
    print(sub(int(argv[1]), int(argv[2])))
    print(div(int(argv[1]), int(argv[2])))
    print(mul(int(argv[1]), int(argv[2])))
    
else:
    print("사용법: calc_test 숫자1 숫자2")