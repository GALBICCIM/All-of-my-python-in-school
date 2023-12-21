import sys


def tri_area(width, height):
    return width * height * 1/2


def box_area(width, height):
    return width * height


# 삼각형, 사각형의 넒이를 출력하는 함수
def print_area(width, height):
    print("가로", width, "세로", height, "인 삼각형의 넒이 : ",
        tri_area(width, height))
    
    print("가로", width, "세로", height, "인 사각형의 넒이 : ",
        box_area(width, height))
    
    
if __name__ == "__main__":
    if len(sys.argv) == 3:
        print_area(int(sys.argv[1]), int(sys.argv[2]))
        
    else:
        print("python area.py 가로 세로")