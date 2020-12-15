curr_rate_sem = 45000
annual_rate = 90000
plan_increase = 1.3
annual_rate_for = 0
sem_forecast = annual_rate_for/2
for year in range(1,6):
    annual_rate_for = annual_rate*plan_increase
    annual_rate = annual_rate_for
    sem_forecast = annual_rate_for/2
    print(year, sem_forecast)