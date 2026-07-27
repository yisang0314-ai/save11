a = int(input("1.숫자를 입력: "))
b = int(input("2.숫자를 입력: "))
c = int(input("3.(1) 더하기 (2) 빼기 (3) 나누기 (4) 곱하기 를 입력: "))

if c == 1:
    print(a + b)
elif c == 2:
    print(a - b)
elif c == 3:
    print(a / b)
elif c == 4:
    print(a * b)
else:
    print("잘못된 번호입니다.")
