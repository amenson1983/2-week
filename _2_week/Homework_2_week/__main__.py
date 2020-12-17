from _2_week.Homework_2_week.Library import burn_kikal, budg_analys, dist_don, rain_thic, cels_to_far, \
    salary_p_day, sum_positive_, ocean_riise, edu_rate_increase, mass_loose, factorial_calc, population_incr, uzor_11, \
    uzor_22, kilom_konvert, tax_calc_, ins_min_sum, car_expen, tax_estate_calculation, calor_f_c, incom_stadium_seats, \
    paint_calculation, sales_tax_calculate, foot_inch_convert, math_test, max_of_two, falling_distance, \
    cynetic_energy_calc, aver_grade, chet_nechet_count, simple_figure_calc, mist_collect

def main():
    print("Добрый день, Максим, ниже представлен список выполненных домашних заданий на вторую неделю:")
    print("\t\tГЛАВА 4", "\t\t\t\t\t\t\t\tГЛАВА 5")
    print("*" * 80)
    print("1. \tСборщик ошибок", "\t\t\t\t\t\t\t16.Конвертер километров")
    print("2. \tСожженные калории", "\t\t\t\t\t\t17.Модернизация программы расчета налога с продаж")
    print("3. \tАнализ бюджета", "\t\t\t\t\t\t\t18.Какова стоимость страховки?")
    print("4. \tПройденное расстояние", "\t\t\t\t\t19.Расходы на автомобиль")
    print("5. \tСредняя толщина дождевых осадков", "\t\t20.Налог на недвижимое имущество")
    print("6. \tТаблица соответствия между,", "\t\t\t21.Калории за счёт жиров и углеводов",
          "\n\tградусами Цельсия и Фаренгейта")
    print("7. \tМелкая монета для зарплаты", "\t\t\t\t22.Сидячие места на стадионе")
    print("8. \tСумма чисел", "\t\t\t\t\t\t\t23.Оценщик малярных работ")
    print("9. \tУровень океана", "\t\t\t\t\t\t\t24.Месячный налог с продаж")
    print("10. Рост платы за обучение", "\t\t\t\t\t25.Футы в дюймы")
    print("11. Потеря массы", "\t\t\t\t\t\t\t26.Математический тест")
    print("12. Вычисление факториала числа", "\t\t\t27.Максимальное из двух значений")
    print("13. Популяция", "\t\t\t\t\t\t\t\t28.Высота падения")
    print("14. Узор-1", "\t\t\t\t\t\t\t\t\t29.Кинетическая энергия")
    print("15. Узор-2", "\t\t\t\t\t\t\t\t\t30.Средний балл и его уровень")
    print("\t\t\t\t\t\t\t\t\t\t\t31.Счётчик четных/нечетных чисел")
    print("\t\t\t\t\t\t\t\t\t\t\t32.Простые числа")
    print("0. ВЫХОД")
    choice = int(input("Выберите задание на проверку: "))
    while choice != 0:
        if choice == 1:
            mist_collect()
        elif choice == 2:
            burn_kikal()
        elif choice == 3:
            budg_analys()
        elif choice == 4:
            dist_don()
        elif choice == 5:
            rain_thic()
        elif choice == 6:
            cels_to_far()
        elif choice == 7:
            salary_p_day()
        elif choice == 8:
            sum_positive_()
        elif choice == 9:
            ocean_riise()
        elif choice == 10:
            edu_rate_increase()
        elif choice == 11:
            mass_loose()
        elif choice == 12:
            factorial_calc()
        elif choice == 13:
            population_incr()
        elif choice == 14:
            uzor_11()
        elif choice == 15:
            uzor_22()
        elif choice == 16:
            kilom_konvert()
        elif choice == 17:
            tax_calc_()
        elif choice == 18:
            ins_min_sum()
        elif choice == 19:
            car_expen()
        elif choice == 20:
            tax_estate_calculation()
        elif choice == 21:
            calor_f_c()
        elif choice == 22:
            incom_stadium_seats()
        elif choice == 23:
            paint_calculation()
        elif choice == 24:
            sales_tax_calculate()
        elif choice == 25:
            foot_inch_convert()
        elif choice == 26:
            math_test()
        elif choice == 27:
            max_of_two()
        elif choice == 28:
            falling_distance()
        elif choice == 29:
            cynetic_energy_calc()
        elif choice == 30:
            aver_grade()
        elif choice == 31:
            chet_nechet_count()
        elif choice == 32:
            simple_figure_calc()
        elif choice == 0:
            print("До свидания!")

main()
