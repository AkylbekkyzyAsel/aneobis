a = input()
a1 = list(a)
for i in a1:
    b1 = int(i)
    if (b1 % 2 == 0): a1.remove(i)
print(str(a1))
print(' '.join(map(str, a1)))   