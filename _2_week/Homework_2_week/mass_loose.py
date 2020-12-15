mass_base = float(input("Введите свою массу: "))
loose_kg = 1.5
print("Месяц \t\tНовый вес")
print("*"*21)
for month in range(1,7,1):
    mass_base = mass_base-loose_kg
    print(month, "\t\t\t", mass_base)