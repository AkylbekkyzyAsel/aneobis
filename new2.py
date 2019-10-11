a = input()
b = a.split(" ")
x = int(b[0])
y = int(b[1])
z = int(b[2])
r = float(x+y+z)/3
print(x,"+", y, "+", z, "=", x+y+z, sep="")
print(x,"*", y, "*", z, "=", x*y*z, sep="")
print("(", x,"+", y, "+", z, ")/3", "=", float('{:.3f}'.format(r)), sep="")

