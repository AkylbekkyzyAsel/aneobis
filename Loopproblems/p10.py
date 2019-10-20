a = input()
b = int(a)

for num* in range(1, b+1):
    r = num*num
    r1 = list(str(num))
    r2 = list(str(r))
    i = 0
    q = 0
    while i < len(str(num)):
        if(r1[len(r1)-1-i] == r2[len(r2)-1-i]): q += 1
        i += 1
    if(q == len(str(num))): print(num,"*",num,"=",r,sep="")
        
    