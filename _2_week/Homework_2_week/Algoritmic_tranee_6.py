znamen_ = int(input("Введите конечное число ряда знаменателя (целое):"))
nach_chisl = int(input("Введите начальное число ряда числителя (целое):"))
kon_chisl = int(input("Введите конечное число ряда числителя (целое):"))
shag_chisl = int(input("Введите шаг ряда числителя (целое):"))
sum_ = 0
if znamen_ > 0:
    for x in range(nach_chisl,kon_chisl+1,shag_chisl):
        sum_ += x/znamen_
        znamen_ -=1
    print(sum_)
else: print("Zero divizion")
