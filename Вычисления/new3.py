import math  
a = input()
b = input()
a1 = a.split(" ")
b1 = b.split(" ")
x1 = float(a1[0])
x2 = float(b1[0])
y1 = float(a1[1])
y2 = float(b1[1])
x = x1-x2
y = y1-y2
print(float('{:.3f}'.format(math.sqrt(x*x + y*y))))