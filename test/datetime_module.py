from datetime import datetime


td = datetime.now()

print(td)


print(td.year, "년", sep = "", end = " ")
print(td.month, "월", sep = "", end = " ")
print(td.day, "일", sep = "", end = " ")
print(td.hour, "시", sep = "", end = " ")
print(td.minute, "분", sep = "", end = " ")
print(td.second, "초", sep = "", end = " ")
print("요일 : ", td.weekday())


day = datetime(2023, 12, 25, 0, 0, 0)
print(day.strftime("%A"))

print("크리스마스까지 남은 기간 : ", day - td)