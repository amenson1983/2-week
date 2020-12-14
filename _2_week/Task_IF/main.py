from _2_week.Task_IF.task_if_lib import task4, task02_print_max_value, task02_print_min_value, task02_print_max_count, \
    task01_print_min_value

print("1. Даны 4 числа типа int. Сравнить их и вывести наименьшее на консоль.")
print("2. Вывести на консоль количество максимальных чисел среди этих четырех.")
print("3. Даны 5 чисел типа int. Сравнить их и вывести наименьшее и наибольшее на консоль.")
print("4. Даны имена 2 человек. Если имена равны - тезки.")
print("press any int value for exit")
answer = input()
if answer == "1":
    task01_print_min_value()
elif answer == "2":
    task02_print_max_count()
elif answer == "3":
    task02_print_min_value()
    task02_print_max_value()
elif answer == "4":
    task4()
else:
    print("No task no problem. Good bye...")

