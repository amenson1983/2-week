def chet_nechet_count():
    import random
    chet = 0
    nechet = 0
    total = 0
    while total < 100:
        for num in [random.randint(1,101)]:
            x = num%2
            total += 1
            if x == 0:
                chet +=1
            else: nechet +=1
    print("Количество чётных: ",chet, "\nКоличество нечётных: ", nechet, "\nКоличество сгенерированных чисел: ",total)

