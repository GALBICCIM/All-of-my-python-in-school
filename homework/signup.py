id = input("아이디를 지정하세요. : ")
pw = input("비밀번호를 지정하세요. : ")

loginid = input("아이디를 입력하세요. : ")
loginpw = input("비밀번호를 입력하세요. : ")

if id == loginid and pw == loginpw:
    print("로그인 성공")
else:
    print("아이디 혹은 비밀번호가 틀렸습니다.")