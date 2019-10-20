a = input()
b = a.split(" ")
b1 = int(b[0])
b2 = int(b[1])
for number in range(b1 - 1, b2):
    print(number + 1,"*", number + 1, "=", (number + 1)*(number+1))
