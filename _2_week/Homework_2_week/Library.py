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