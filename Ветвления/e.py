a = input()
b = a.split(" ")
x = int(b[0])
y = int(b[1])
z = int(b[2])

m = max(x, y, z)

if(m == x):
    if(z + y >= x): print("YES")
    else: print("NO")
elif(m == y):
    if(x + z >= y): print("YES")
    else: print("NO")
elif(m == z):
    if(x + y >= z): print("YES")
    else: print("NO")

