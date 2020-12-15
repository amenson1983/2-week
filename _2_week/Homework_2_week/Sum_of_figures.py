row = 0
sum = 0
while row >= 0:
    row = int(input("Введите положительное число 'отрицательное означает выход': "))
    if row < 0:
        break
    sum +=row
print("Сумма = ", sum)