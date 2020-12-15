temp_far = 0
print("Цельсий\t\tФаренгейт")
print("*"*22)
for temp in range(0,21,1):
    temp_far = ((9*temp)/5)+32
    print(temp,"\t\t",temp_far)