# + 연산자를 사용하면 문자열을 이어줌.
text1 = "Exam" + "Fighting!"
print(text1)


# * 연산자를 사용하면 문자열을 반복함.
text2 = "Fuck" * 3
print(text2)


# 따옴표(")를 세개 쓰면 여러줄을 입력할 수 있다.
text3 = """This is
Elon
Musk"""
print(text3)


print("안녕", "하세요", end = "ㅎㅎ \n")
# 결과 - 안녕 하세요ㅎㅎ


print("안녕", "하세요", "여러분", sep="ㅎㅎ")
# 결과 - 안녕ㅎㅎ하세요ㅎㅎ여러분


str = "test sentence"

# 슬라이싱: 문자열에서 원하는 부분을 잘라서 가져온다
print(str[3:7])
# 결과 - t se


# 인덱스 1을 쓰지 않으면 맨 앞에서부터 가져온다
print(str[:7])
# 결과 - test se


# 인덱스 2를 쓰지 않으면 맨 뒤까지 가져온다
print(str[3:])
# 결과 - t sentence


# 인덱스 1, 2 둘 다 없으면 전체 문자열을 가져온다
print(str[:])
# 결과 - test sentence


# 슬라이싱 구간에 문자가 없을 때는 빈 문자열을 가져온다
print(str[7:3])
# 결과 - 


# 음수 인덱스도 사용 가능하다
print(str[-9:10])
# 결과 -  sente

if <조건문>:
    수행할 문장 1
    수행할 문장 2
    
elif:
    수행할 문장 A
    수행할 문장 B
else:
    수행할 문장 I
    수행할 문장 II