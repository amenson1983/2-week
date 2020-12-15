q_days = int(input("Введите количество дней: "))
day_pay = 1
sum_coin = 0
sum_hrn = 0
print("День\t\tЗарплата")
print("*" * 20)
for day in range(1,q_days+1,1):
    day_pay = day_pay*2
    sum_coin +=day_pay
    print(day, "\t\t\t", day_pay)
sum_hrn = sum_coin / 100
print("Общая з/п до вычета налогов: ", sum_hrn, "грн")