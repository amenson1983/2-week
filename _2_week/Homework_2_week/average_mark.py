from _2_week.Homework_2_week.Library import calc_aver_, determine_grade
average,a,b,c,d,e = calc_aver_()
for num in [a,b,c,d,e]:
    grade = determine_grade(num)
    print(num, grade)
print("Средний балл: ",average)




