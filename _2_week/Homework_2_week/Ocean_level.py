mm_per_year = 1.6
sum = 0
print("Год\t\tПоднятие от изначальной точки")
print("*"*35)
for years in range(1,26,1):
    sum += mm_per_year
    print(years,"\t\t\t\t", round(sum,2))
