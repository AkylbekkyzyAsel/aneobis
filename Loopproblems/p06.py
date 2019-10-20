a = input()
b = list(a)
i = 0;
q = 0
while i < len(b) - 1:
    if(int(b[i]) == int(b[i+1])):
        q += 1
    i += 1    
if q >= 1: print("YES")
else: print("NO")        
