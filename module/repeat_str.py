import sys


def repeat_str(msg, n):
    
    return msg * n
    
    
if __name__ == "__main__":
    if len(sys.argv) == 3:
        print(repeat_str(sys.argv[1], int(sys.argv[2])))
    
    else:
        print("python repeat_str.py 문자열 양의 정수")