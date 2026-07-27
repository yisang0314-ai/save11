n = int(input("측정횟수: "))
count = 0

for i in range(n):
    value = int(input("측정값: "))
    if 80 < n:
        count += 1
print("초과 개수: ", count)
