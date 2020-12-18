from _2_week.Homework_2_week.Library import list_simple

def simple_fig_list():
    for num in range(2, 101, 1):
        list_simple(num)
        x = list_simple(num)
        if x != None:
            print(x, end=" ")


