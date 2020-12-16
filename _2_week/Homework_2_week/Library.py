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

def ocean_riise():
    mm_per_year = 1.6
    sum = 0
    print("Год\t\tПоднятие от изначальной точки")
    print("*" * 35)
    for years in range(1, 26, 1):
        sum += mm_per_year
        print(years, "\t\t\t\t", round(sum, 2))

def edu_rate_increase():
    curr_rate_sem = 45000
    annual_rate = 90000
    plan_increase = 1.3
    annual_rate_for = 0
    sem_forecast = annual_rate_for / 2
    for year in range(1, 6):
        annual_rate_for = annual_rate * plan_increase
        annual_rate = annual_rate_for
        sem_forecast = annual_rate_for / 2
        print(year, sem_forecast)

def mass_loose():
    mass_base = float(input("Введите свою массу: "))
    loose_kg = 1.5
    print("Месяц \t\tНовый вес")
    print("*" * 21)
    for month in range(1, 7, 1):
        mass_base = mass_base - loose_kg
        print(month, "\t\t\t", mass_base)

def factorial_calc():
    number = int(input("Введите не отрицательное число: "))
    factorial = 1
    inter = 1
    if number <= 0:
        print("Я сказал - НЕ ОТРИЦАТЕЛЬНОЕ!")
    else:
        for part in range(1, number + 1, 1):
            inter *= part
    print(inter)

def population_incr():
    quant = int(input("Стартовое количество организмов: "))
    increase = int(input("Среднесуточное увеличение (%): "))
    increase_percent = 1 + (increase / 100)
    days = int(input("Количество дней для размножения: "))
    print("День\t\t\tПопуляция")
    print("*"*24)
    for day in range(1, days + 1, 1):
        print(day,"\t\t",round(quant,4))
        quant *= increase_percent

def uzor_11():
    for num in range(7, 0, -1):
        print("*" * num)

def uzor_22():
    print("#", "#")
    for num in range(0, 5, 1):
        print("#", " " * num, "#")

def percentage_from_(amount, rate):
    percentage = amount * (rate / 100)
    return percentage

def get_name_surname():
    name = input("Введите своё имя: ")
    surname = input("Введите свою фамилию: ")
    return surname, name

def kilom_convert(x):
        miles = round((x*0.6214),2)
        return miles

def kilom_konvert():
    km = float(input("Введите расстояние в километрах:"))
    print("Расстояние в км: ", km, "\nРасстояние в милях:", kilom_convert(km))

def get_amount_calc_tax():
    x = float(input("Введите сумму покупки: "))
    fed = x*0.05
    reg = x*0.025
    return x, fed, reg

def tax_calc_():
    amount, federal, regional = get_amount_calc_tax()
    amount += federal + regional
    print("Общая сумма:", amount,
          "\nВ том числе налоги:", "\nФедеральный налог: ", federal, "\nРегиональный налог: ", regional)