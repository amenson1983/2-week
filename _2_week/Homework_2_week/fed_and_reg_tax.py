from _2_week.Homework_2_week.Library import get_amount_calc_tax

amount, federal, regional = get_amount_calc_tax()
amount += federal + regional
print("Общая сумма:", amount,
      "\nВ том числе налоги:", "\nФедеральный налог: ", federal, "\nРегиональный налог: ", regional)