summary = 0
credit = float(input('Введите расходы по кредиту в месяц: '))
insurance = float(input('Введите расходы на страховку в месяц: '))
fuel = float(input('Введите расходы на топливо в месяц: '))
oil = float(input('Введите расходы на машинное масло в месяц: '))
tires = float(input('Введите расходы на шины в месяц: '))
tech = float(input('Введите расходы на ТО в месяц: '))
for num in [credit, insurance, fuel, oil, tires, tech]:
    summary +=num
print("Стоимость обслуживания в месяц: ", summary, "грн"
        "\nСтоимость годового обслуживания: ", summary*12, "грн")