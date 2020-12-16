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

def insur_min_amou():
    x = float(input("Введите стоимость строения: "))
    min_am = x * 0.8
    return x, min_am

def ins_min_sum():
    cost, min_ins_am = insur_min_amou()
    print("Общая стоимость строения:", cost,
          "\nМинимальная сумма замещения: ", min_ins_am)

def car_expen():
    summary = 0
    credit = float(input('Введите расходы по кредиту в месяц: '))
    insurance = float(input('Введите расходы на страховку в месяц: '))
    fuel = float(input('Введите расходы на топливо в месяц: '))
    oil = float(input('Введите расходы на машинное масло в месяц: '))
    tires = float(input('Введите расходы на шины в месяц: '))
    tech = float(input('Введите расходы на ТО в месяц: '))
    for num in [credit, insurance, fuel, oil, tires, tech]:
        summary += num
    print("Стоимость обслуживания в месяц: ", summary, "грн"
                                                       "\nСтоимость годового обслуживания: ", summary * 12, "грн")
def insur_min_amou1():
    x = float(input("Введите стоимость строения: "))
    eval_cost = x * 0.6
    return x, eval_cost

def tax_estate_calculation():
    tot_cost, eval_cost = insur_min_amou1()
    tax_100 = 0.72 * (eval_cost / 100)
    print("Фактическая соимость недвижимости: ", tot_cost, "$", "\nОценочная соимость недвижимости: ", eval_cost, "$",
          "\nСумма налогов к уплате: ", round(tax_100, 2), "$")

def calor_calc():
    fats = float(input("Введите количество грамм жиров, которое Вы употребили за день: "))
    carbohydrades = float(input("Введите количество грамм углеводов, которое Вы употребили за день: "))
    calor_fats = fats * 9
    calor_carbohyd = carbohydrades * 4
    return calor_fats, calor_carbohyd

def calor_f_c():
    calor_fr_fats, calor_from_carbo = calor_calc()
    print("Калории полученные от жиров", calor_fr_fats, "\nКалории полученные от углеводов", calor_from_carbo)

def get_quant_seats():
    class_a= int(input("Введите количество проданных билетов на места класса А: "))
    class_b = int(input("Введите количество проданных билетов на места класса B: "))
    class_c = int(input("Введите количество проданных билетов на места класса C: "))
    income_a = class_a*20
    income_b = class_b*15
    income_c = class_c*10
    return income_a, income_b, income_c

def incom_stadium_seats():
    a, b, c = get_quant_seats()
    print("Доход от продажи мест класса А:", a, "грн", "\nДоход от продажи мест класса В:", b, "грн",
          "\nДоход от продажи мест класса С:", c, "грн")

def paint_work_calc():
    sq_m = float(input("Введите количество квадратных метров для покраски: "))
    paint_price = float(input("Введите цену краски (5л): "))
    paint_price1l = paint_price / 5
    work_cost1h = 2000
    need_paint = (sq_m / 10) * 5
    need_paint5l = need_paint / 5
    need_work = (sq_m / 10) * 8
    paint_cost = need_paint * paint_price1l
    work_cost = need_work * work_cost1h
    return need_paint5l, need_work, paint_cost, work_cost

def paint_calculation():
    total_cost = 0
    quant_5l_paint, work_hours, paint_cost, work_cost = paint_work_calc()
    total_cost += paint_cost + work_cost
    print("Количество 5л банок: ", quant_5l_paint, "шт", "\nКоличество часов на работу: ", work_hours, "часов",
          "\nСтоимость краски: ", paint_cost, "грн", "\nСтоимость работы: ", work_cost, "грн", "\nИТОГО: ", total_cost,
          "грн")
def get_sales_calc_tax():
    x = float(input("Введите сумму продажи: "))
    fed = x*0.05
    reg = x*0.025
    return fed, reg

def tax_sales_calc_():
    federal, regional = get_sales_calc_tax()
    amount_tax = 0
    amount_tax += federal + regional
    print("Общая сумма налогов:", amount_tax,
          "\nВ том числе:", "\nФедеральный налог: ", federal, "\nРегиональный налог: ", regional)

def sales_tax_calculate():
    amount = 0
    print = tax_sales_calc_()

def foot_convert():
    foot = float(input("Введите расстояние в километрах:"))
    inch = round((foot * 12), 2)
    return foot,inch

def foot_inch_convert():
    foot, inch = foot_convert()
    print("Длинна в футах: ", foot, "\nДлина в дюймах:", inch)

def math_test():
    import random
    num1 = random.randint(1, 1000)
    num2 = random.randint(1, 1000)
    total = num1 + num2
    print("\n\t", num1, "\n+\t", num2, "\n=\t")
    answer = int(input("Введите ответ:"))
    if answer == total:
        print("Поздравляем, ответ верный!")
    else:
        print("\n\t", num1, "\n+\t", num2, "\n=\t", total)

def max_of_two():
    num1 = int(input("Введите число 1: "))
    num2 = int(input("Введите число 2: "))
    max_ = max(num1, num2)
    print(max_)

def falling_distance():
    print("СЕКУНДА\t\t\tМЕТРОВ ПОЛЕТА")
    print("*" * 25)
    for time_s in range(1, 11, 1):
        time_sec = time_s
        g = 9.8
        distance = 1 / 2 * (g * (time_sec ** 2))
        print(time_sec, "\t\t\t\t", round(distance, 2))

def cynetic(m,v):
    energy = 1/2*(m*(v**2))
    return energy

def cynetic_energy_calc():
    mass = float(input("Введите массу тела, кг: "))
    speed = float(input("Введите скорость, м\с: "))
    energy = cynetic(mass, speed)
    print("Кинетическая энергия: ", round(energy, 2))

def calc_aver_():
    a = int(input("Введите оценку 1: "))
    b = int(input("Введите оценку 2: "))
    c = int(input("Введите оценку 3: "))
    d = int(input("Введите оценку 4: "))
    e = int(input("Введите оценку 5: "))
    sum = a + b + c + d + e
    aver_ = sum / 5
    return aver_,a,b,c,d,e

def determine_grade(classif):
    grade = ""
    if classif < 60:
        grade = "F"
    elif classif >=60 and classif <70:
        grade = "D"
    elif classif>=70 and classif<80:
        grade = "C"
    elif classif>=80 and classif<90:
        grade = "B"
    else: grade = "A"
    return grade
def aver_grade():
    average, a, b, c, d, e = calc_aver_()
    for num in [a, b, c, d, e]:
        grade = determine_grade(num)
        print(num, grade)
    print("Средний балл: ", average)