id = "admin"
pw1 = "1234"
pw2 = "5678"

user_id = input("아이디 입력: ")
user_pw = input("비밀번호 입력: ")

if id == user_id and (pw1 == user_pw or pw2 == user_pw):
    print("로그인 성공")
else:
    print("로그인 실패")
