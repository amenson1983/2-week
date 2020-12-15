def division_of_2_rows(x,y):
        Div_2_rows()

def Div_2_rows():
    znamen_ = int(input("Введите конечное число ряда знаменателя (целое):"))
    nach_chisl = int(input("Введите начальное число ряда числителя (целое):"))
    kon_chisl = int(input("Введите конечное число ряда числителя (целое):"))
    shag_chisl = int(input("Введите шаг ряда числителя (целое):"))
    sum_ = 0
    if znamen_ > 0:
        for x in range(nach_chisl, kon_chisl + 1, shag_chisl):
            sum_ += x / znamen_
            znamen_ -= 1
        print(sum_)
    else:
        print("Zero divizion")

def mistake_collect():
    days = int(input("Сколько дней будем обозревать?"))
    summary = 0
    for x in range(days):
        mist_day = int(input("Введите количество ошибок за день: "))
        summary += mist_day
    print("Общее количество ошибок: ", summary)

def burn_kikal():
    kkal_per_min = float(input("Введите количество Ккал, сжигаемых в минуту: "))
    for minutes in range(10, 31, 5):
        kkal = minutes * kkal_per_min
        print(kkal)

def budg_analys():
    amount_ = float(input("Введите сумму Вашего бюджета на месяц: "))
    summary = 0
    conclusion = 0
    food = float(input('Введите расходы на еду: '))
    trans = float(input('Введите расходы на транспорт: '))
    paym = float(input('Введите расходы на комунальные платежи: '))
    clothes = float(input('Введите расходы на одежду: '))
    rest = float(input('Введите другие расходы: '))
    for num in [food, trans, paym, clothes, rest]:
        summary += num
    if summary < amount_:
        print("Экономия составляет: ", amount_ - summary, "грн")
    elif summary > amount_ or summary == amount_:
        print("Дефицит составляет: ", amount_ - summary, "грн")