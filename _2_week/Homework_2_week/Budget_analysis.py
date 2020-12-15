amount_ = float(input("Введите сумму Вашего бюджета на месяц: "))
summary = 0
conclusion = 0
food = float(input('Введите расходы на еду: '))
trans = float(input('Введите расходы на транспорт: '))
paym = float(input('Введите расходы на комунальные платежи: '))
clothes = float(input('Введите расходы на одежду: '))
rest = float(input('Введите другие расходы: '))
for num in [food,trans,paym,clothes,rest]:
        summary +=num
if summary < amount_:
    print("Экономия составляет: ", amount_-summary, "грн")
elif summary > amount_ or summary == amount_:
    print("Дефицит составляет: ", amount_-summary, "грн")