a = 2
b = 3
c = 3
d = 1
max = 0
if a >= b and a>=c and a>=d:
    max = a
elif b >= a and b>=c and a>=d:
    max = b
elif c >= a and c>=b and c>=d:
    max = c
else: max = d
print(max)

num = 0
num1 = 0
if max == a or max == b:
   num = 1

if max ==c or max == d:
    num1 = 1
count = num + num1
print(count)
