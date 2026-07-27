n = int(input("숫자를 입력: "))

total = 0
for n in range(n + 1):
    total += n

for j in range(n + 1):
    if j % 2 == 0:
        total += j
print("합:", total)
