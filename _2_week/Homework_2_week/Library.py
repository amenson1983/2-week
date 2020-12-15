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

def dist_don():
    dist = 0
    speed = int(input("Введите скорость транспортного средства (км\ч): "))
    time = int(input("Сколько часов оно двигалось?: "))
    print("Час\tПройденное расстояние")
    print("*" * 25)
    for hour in range(0, time + 1, 1):
        dist = hour * speed
        print(hour, "\t", dist)

def rain_thic():
    years = int(input("Укажите количество лет: "))
    tot_thick = 0
    month_quant = 0
    for yea in range(0, years, 1):
        for mon in range(12):
            rain_thick = int(input("Введите толщину осадков для месяца"))
            tot_thick += rain_thick
    month_quant = years * 12
    average = tot_thick / (years * 12)
    print("Средняя толщина осадков за период в месяц: ", average)
    print("Общяя толщина осадков за период: ", tot_thick)
    print("Общее количество месяцев: ", month_quant * years)

def cels_to_far():
    temp_far = 0
    print("Цельсий\t\tФаренгейт")
    print("*" * 22)
    for temp in range(0, 21, 1):
        temp_far = ((9 * temp) / 5) + 32
        print(temp, "\t\t", temp_far)

def salary_p_day():
    q_days = int(input("Введите количество дней: "))
    day_pay = 1
    sum_coin = 0
    sum_hrn = 0
    print("День\t\tЗарплата")
    print("*" * 20)
    for day in range(1, q_days + 1, 1):
        day_pay = day_pay * 2
        sum_coin += day_pay
        print(day, "\t\t\t", day_pay)
    sum_hrn = sum_coin / 100
    print("Общая з/п до вычета налогов: ", sum_hrn, "грн")

def sum_positive_():
    row = 0
    sum = 0
    while row >= 0:
        row = int(input("Введите положительное число 'отрицательное означает выход': "))
        if row < 0:
            break
        sum += row
    print("Сумма = ", sum)