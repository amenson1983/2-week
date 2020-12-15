quant = int(input("Стартовое количество организмов: "))
increase = int(input("Среднесуточное увеличение (%): "))
increase_percent = 1+(increase/100)
days = int(input("Количество дней для размножения: "))
for day in range(1,days+1,1):
    print(day, quant)
    quant *=increase_percent
