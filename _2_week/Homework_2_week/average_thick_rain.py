years = int(input("Укажите количество лет: "))
tot_thick = 0
month_quant = 0
for yea in range(0,years,1):
    for mon in range(12):
        rain_thick = int(input("Введите толщину осадков для месяца"))
        tot_thick +=rain_thick
month_quant = years*12
average = tot_thick/(years*12)
print("Средняя толщина осадков за период в месяц: ",average)
print("Общяя толщина осадков за период: ",tot_thick)
print("Общее количество месяцев: ", month_quant*years)