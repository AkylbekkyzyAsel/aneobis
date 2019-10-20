a = int(input())
list = []
m = a / 1000
list.append('M' * int(m))
d = a % 1000 / 500
print(d)
list.append('D' * int(d))
c = (a - m - d) / 100
list.append('C' * int(c))
l = (a - m - d - c) / 50
list.append('L' * int(l))
x = (a - m - d - c - l) / 10
list.append('X' * int(x))
i = (a - m - d - c - l) / 1
list.append('I' * int(i))
str1 = ''.join(list)
print(str1)
 

