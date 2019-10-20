a = input()

for i in a:
    a1 = int(i)
    if a1 % 2 == 0: a.replace(a1,'')
print(a)    