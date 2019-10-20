a = input()
a1 = int(a)
c = input()
b = c.split(" ")
i = 0
r = 0
e = 0
while i < len(b):
    b1 = int(b[i])
    if b1 == 0: e += 1
    r += b1
    i += 1
print(r)
if e >= 1: print("NO")
else: print("YES")   