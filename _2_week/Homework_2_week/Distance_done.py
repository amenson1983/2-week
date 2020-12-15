dist = 0
speed = int(input("Введите скорость транспортного средства (км\ч): "))
time = int(input("Сколько часов оно двигалось?: "))
print("Час\tПройденное расстояние")
print("*" * 25)
for hour in range(0,time+1,1):
    dist = hour*speed
    print(hour,"\t",dist)