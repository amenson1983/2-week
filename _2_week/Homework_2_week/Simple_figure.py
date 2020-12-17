def simple_figure_calc():
    figure = int(input("Введите целое число: "))
    defin = 0
    for num in range(2, figure + 1, 1):
        middle = figure % num
        if middle == 0:
            defin += 1
    if defin > 1:
        print("Число не является простым")
    else:
        print("Число является простым")