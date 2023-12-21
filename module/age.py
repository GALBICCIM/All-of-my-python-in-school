name = input("이름을 입력 해주세요: ")
age = int(input("나이를 입력 해주세요: "))

print(name + "님의 나이는 " + str(age) + "세 입니다.")
print("{0}님의 나이는 {1}세 입니다.".format(name, age))
print("내년 나이 : ", age + 1)