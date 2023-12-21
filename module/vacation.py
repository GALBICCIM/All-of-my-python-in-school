from datetime import datetime


today = datetime.now()
vacation_day = datetime(2023, 12, 29, 0, 0, 0)

# print("현재 날짜 : " + str(today.year), today.month, today.day, sep = "-")
# print("현재 날짜 : {0}-{1}-{2}".format(today.year, today.month, today.day))
# print(f"현재 날짜: {today.year}-{today.month}-{today.day}")

print("현재 날짜:", today.date())
print("방학 까지 남은 일 수:", vacation_day - today)