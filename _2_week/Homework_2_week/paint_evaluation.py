from _2_week.Homework_2_week.Library import paint_work_calc

total_cost = 0
quant_5l_paint, work_hours, paint_cost, work_cost = paint_work_calc()
total_cost +=paint_cost+work_cost
print("Количество 5л банок: ",quant_5l_paint,"шт", "\nКоличество часов на работу: ", work_hours,"часов","\nСтоимость краски: ", paint_cost, "грн", "\nСтоимость работы: ",work_cost, "грн","\nИТОГО: ",total_cost,"грн")
