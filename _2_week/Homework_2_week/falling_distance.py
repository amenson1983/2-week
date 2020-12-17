def falling_distance():
    print("СЕКУНДА\t\t\tМЕТРОВ ПОЛЕТА")
    print("*" * 25)
    for time_s in range(1, 11, 1):
        time_sec = time_s
        g = 9.8
        distance = 1 / 2 * (g * (time_sec ** 2))
        print(time_sec, "\t\t\t\t", round(distance, 2))

falling_distance()

