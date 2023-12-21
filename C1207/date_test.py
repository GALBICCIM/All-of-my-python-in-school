from datetime import datetime


week = ["월", "화", "수", "목", "금", "토", "일"]
td = datetime.now()
exam = datetime(2023, 12, 12, 8, 40, 00)


print(f"{td.year}-{td.month}-{td.day}")
print(f"{td.hour}:{td.minute}:{td.second}")
print(week[td.weekday()])


print(exam - td)