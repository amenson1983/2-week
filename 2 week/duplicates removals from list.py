list = ['Joe', 'Billy', 'Corey', 'Joe']
uniques = []
for name in list:
    if name not in uniques:
        uniques.append(name)
print(uniques)