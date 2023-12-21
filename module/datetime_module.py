from datetime import datetime


today = datetime.now()
# print(today)

# print(today.year, "년", sep = "", end = " ")
# print(today.month, "월", sep = "", end = " ")
# print(today.day, "일", sep = "", end = " ")

# print(today.hour, "시", sep = "", end = " ")
# print(today.minute, "분", sep = "", end = " ")
# print(today.second, "초", sep = "", end = " ")
# print("요일 : ", today.weekday())


# day = datetime(2023, 11, 20, 0, 0, 0)

# print(day.year, "년", sep = "", end = " ")
# print(day.month, "월", sep = "", end = " ")
# print(day.day, "일", sep = "", end = " ")
# print(day.hour, "시", sep = "", end = " ")
# print(day.minute, "분", sep = "", end = " ")
# print(day.second, "초", sep = "", end = " ")
# print("요일 : ", day.weekday())

# print(today - day)


print("{0}년 {1}월 {2}일 {3}시 {4}분 {5}초".format(today.year, today.month, today.day, today.hour, today.minute, today.second))