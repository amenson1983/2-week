from _2_week.Homework_2_week.Library import cynetic

mass = float(input("Введите массу тела, кг: "))
speed = float(input("Введите скорость, м\с: "))
energy = cynetic(mass,speed)
print(round(energy,2))