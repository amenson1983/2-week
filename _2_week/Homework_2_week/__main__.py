from _2_week.Homework_2_week.Library import mistake_collect, burn_kikal, budg_analys, dist_don, rain_thic, cels_to_far

if __name__ == '__main__':
    print("Добрый день, ниже представлен список выполненных домашних заданий на вторую неделю:")
print("1. Сборщик ошибок")
print("2. Сожженные калории")
print("3. Анализ бюджета")
print("4. Пройденное расстояние")
print("5. Средняя толщина дождевых осадков")
print("6. Таблица соответствия между градусами Цельсия и Фаренгейта")


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