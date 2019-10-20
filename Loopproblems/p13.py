a = int(input())
aaa = []

#print(list)
for num in range(1, a+1):
    aoa = list(str(num))
    i = 0
    q = 0
    while i < len(str(num)):
        if(int(aoa[i])!= 0):
            if num % int(aoa[i]) == 0: q += 1
        i += 1
    if(q == len(str(num))): aaa.append(num)    

print(' '.join(map(str, aaa)))          
