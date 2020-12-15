from _2_week.Homework_2_week.Library import mistake_collect

if __name__ == '__main__':
    print("Добрый день, ниже представлен список выполненных домашних заданий на вторую неделю:")
print("1. Сборщик ошибок")
choice = int(input("Выберите задание на проверку: "))
if choice == 1:
    mistake_collect()