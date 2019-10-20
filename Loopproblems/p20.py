a = input()
b = list(a)
i = 0
r = 0

while i < len(a):
    if i % 2 == 0:
        a1 = int(b[i])
        r += a1
    i += 1    
print(r)



