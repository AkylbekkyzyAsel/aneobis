a = input()
b = a.split(" ")
a1 = int(b[0])
a2 = int(b[1])
a3 = int(b[2])
r = int(max(b))
t = int(min(b))
if(a1 == a2 and a1 == a3):
    print("Same age")
elif (r == a1 and r == a2 or a == a1 and r == a3 or r == a3 and r == a2):
    print(t)
    if t == a1: print("Anton")
    elif t == a2: print("Boris")
    else: print("Victor")
elif (t == a1 and t == a2 or t == a1 and t == a3 or t == a3 and t == a2):
    print(r)
    if r == a1: print("Anton")
    elif r == a2: print("Boris")
    else: print("Victor")
else:  
    if r == a1: print("Anton")
    elif r == a2: print("Boris")
    else: print("Victor")
    