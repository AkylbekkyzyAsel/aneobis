a = input()
b = a.split(" ")
a1 = int(b[0])
a2 = int(b[1])
a3 = int(b[2])
if (a1 != 0 or a2 != 0 or a2 != 0): 
    if(a1 + a2 + a3 == 180): print("YES")
else: print("NO")
