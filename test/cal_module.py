from calculator import *


num1 = int(input("자연수 1 : "))
num2 = int(input("자연수 2 : "))


print("{0} + {1} = {2}".format(num1, num2, add(num1, num2)))
print(f"{num1} - {num2} = {sub(num1, num2)}")
print(f"{num1} * {num2} = {multi(num1, num2)}")
print("{0} / {1} = {2}".format(num1, num2, div(num1, num2)))