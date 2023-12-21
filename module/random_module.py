import random


print(random.random()) # 0이상 1미만의 실수 값 (1 미포함)
print(random.uniform(2.5, 10.0)) # 2.5이상, 10.0미만의 실수 값
print(random.randrange(10)) # 0이상 10미만 정수 값
print(random.randrange(1, 7, 2)) # 1이상 7미만, 2씩 증가시킨 정수들 중 하나

season = ["봄", "여름", "가을", "겨울"]
print(random.choice(season))

cards = ["가", "나", "다", "라", "마"]
random.shuffle(cards)
print(cards)

sample = ['1', '2', '3', '4', '5']
print(random.sample(sample, 3))
