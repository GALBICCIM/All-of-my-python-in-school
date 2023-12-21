import random


# 인자값 - 주사위 여러번 굴리게 하자
def rolling_dice(meyon, repeat = 1):
  for r in range(1,repeat + 1):
    n = random.randint(1,meyon)
    print("주사위 굴린 결과",r," : " , n)

rolling_dice(3)

rolling_dice(20, 3)
rolling_dice(repeat = 10, meyon = 4)