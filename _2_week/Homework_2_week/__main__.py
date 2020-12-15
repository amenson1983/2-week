from _2_week.Homework_2_week.Library import mistake_collect, burn_kikal, budg_analys, dist_don, rain_thic, cels_to_far, \
    salary_p_day, sum_positive_, ocean_riise, edu_rate_increase, mass_loose, factorial_calc, population_incr

if __name__ == '__main__':
    print("Добрый день, ниже представлен список выполненных домашних заданий на вторую неделю:")
print("1. Сборщик ошибок")
print("2. Сожженные калории")
print("3. Анализ бюджета")
print("4. Пройденное расстояние")
print("5. Средняя толщина дождевых осадков")
print("6. Таблица соответствия между градусами Цельсия и Фаренгейта")
print("7. Мелкая монета для зарплаты")
print("8. Сумма чисел")
print("9. Уровень океана")
print("10. Рост платы за обучение")
print("11. Потеря массы")
print("12. Вычисление факториала числа")
print("13. Популяция")

choice = int(input("Выберите задание на проверку: "))
if choice == 1:
    mistake_collect()
if choice == 2:
    burn_kikal()
if choice == 3:
    budg_analys()
if choice == 4:
    dist_don()
if choice == 5:
    rain_thic()
if choice == 6:
    cels_to_far()
if choice == 7:
    salary_p_day()
if choice == 8:
    sum_positive_()
if choice == 9:
    ocean_riise()
if choice == 10:
    edu_rate_increase()
if choice == 11:
    mass_loose()
if choice == 12:
    factorial_calc()
if choice == 13:
    population_incr()