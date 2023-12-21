import math


def circle_area(diameter):
    area = math.pi * pow(diameter * 0.5, 2)
    return area

print(circle_area(10))