znamen_ = 30
sum_ = 0
if znamen_ > 0:
    for x in range(1,31,1):
        sum_ += x/znamen_
        znamen_ -=1
    print(sum_)
else: print("Zero divizion")
