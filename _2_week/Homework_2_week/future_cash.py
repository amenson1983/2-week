from _2_week.Homework_2_week.Library import future_cash_


def fut_cah_calc():
    amount = float(input("Введите текущую сумму: "))
    months = float(input("Введите количество месяцев: "))
    rate_ = float(input("Введите ежемесячную процентрую ставку: "))
    rate = rate_ / 100
    future_cash = future_cash_(amount, months, rate)
    print(future_cash)