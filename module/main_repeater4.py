import repeater as r


s = input("반복 할 문자를 입력해주세요. : ")
n = int(input("반복 할 횟수를 입력해주세요. : "))

r.repeat(s, n)
r.repeat(s)
r.once(s)