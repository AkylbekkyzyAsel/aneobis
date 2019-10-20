a = input()
a1 = list(a)
r = 0
if(len(a) % 2 == 1):
    
   
    for i in a1:
        a2 = int(i)
        r += a2
    print(r)        
else:
    i = 0
    while i < len(a1)/2:
        a2 = int(a1[i])
        r += a2
        i += 1
    print(r)
    
    