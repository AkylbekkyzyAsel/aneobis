a = input()
b = list(a)

i = 0
o = 0
e = 0
while i < len(b):
    a1 = int(b[i])
    if(a1 % 2 == 0): e += 1
    else: o += 1
    i += 1
print(o,e)    