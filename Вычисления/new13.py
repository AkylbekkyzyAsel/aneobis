a = input()
b = a.split(" ")
n = int(b[0])
a1 = int(b[1])
d = int(b[2])
an = a1 + (n - 1) * d
s = (a1 + an) / 2 * n
print(int(s / n))    