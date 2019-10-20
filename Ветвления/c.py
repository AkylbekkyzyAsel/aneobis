a = input()
b = a.split(" ")
a1 = int(b[0])
a2 = int(b[1])
a3 = int(b[2])
i = 1
r = 1
t = 1
if (a1 == a2):
    i = i + 1
    if(a1 == a3):
        i = i + 1
    print(i)
        
elif (a1 == a3):
    r = r + 1
    print(r)
elif (a2 == a3):
    t = t + 1
    print(t)
else: print(1)        