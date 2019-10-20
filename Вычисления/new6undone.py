a = input()
e = int(a)
b = e / 3600
c = (e % 3600) / 60
d = e % 3600 % 60
print(int(b), int(c), d)
