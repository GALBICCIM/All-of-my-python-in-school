x = int(input("값을 입력하세요: "))

if 12 < x < 20:
    print(x * x)
else:
    if x < 12:
        print("값이 너무 작습니다.")
    if x > 20:
        print("값이 너무 큽니다.")