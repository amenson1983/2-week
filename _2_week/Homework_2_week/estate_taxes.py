from _2_week.Homework_2_week.Library import insur_min_amou1

tot_cost, eval_cost = insur_min_amou1()
tax_100 = 0.72*(eval_cost/100)
print("Фактическая соимость недвижимости: ",tot_cost, "$","\nОценочная соимость недвижимости: ", eval_cost, "$", "\nСумма налогов к уплате: ", round(tax_100,2), "$")

