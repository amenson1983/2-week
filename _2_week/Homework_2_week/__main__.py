from _2_week.Homework_2_week.Library import mistake_collect, burn_kikal

if __name__ == '__main__':
    print("Добрый день, ниже представлен список выполненных домашних заданий на вторую неделю:")
print("1. Сборщик ошибок")
print("2. Сожженные калории")
choice = int(input("Выберите задание на проверку: "))
if choice == 1:
    mistake_collect()
if choice == 2:
    burn_kikal()