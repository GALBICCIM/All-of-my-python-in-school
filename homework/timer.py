import time
hour = int(input("h: "))
min = int(input("m: "))
sec = int(input("s: "))

while hour != 0:
    hour = hour-1
    time.sleep(3600)
    print(hour)
    
while min != 0:
    min = min-1
    time.sleep(60)
    print(min)
    
while sec != 0:
    sec = sec-1
    time.sleep(1)
    print(sec)