a = input()
b = a.split(" ")
b1 = int(b[0])
b2 = int(b[1])
r = []
for num in range(b1, b2+1):
    i = 1;
    c = 0
    while i <= num:
        if(num % i == 0): 
            c += 1
        i += 1
    if(c == 2): 
        r.append(num)
print(' '.join(map(str, r)))    