# n = int(input("숫자를 입력: "))

# total = 0
# for j in range(n + 1):
#    if j % 2 == 0 or j % 3 == 0:
#        print(j)

# for j in range(n + 1):
#    if j % 2 == 0 or j % 3 == 0:
#        total += j

total1, total2, total3

for j in range(2, n + 1, 2):
    total1 += j

for j in range(3, n + 1, 3):
    total2 += j

for j in range(6, n + 1, 6):
    total3 += j
