number = int(input("Введите не отрицательное число: "))
factorial = 1
inter = 1
if number <= 0:
    print("Я сказал - НЕ ОТРИЦАТЕЛЬНОЕ!")
else:
    for part in range(1,number+1,1):
        inter *= part
print(inter)
