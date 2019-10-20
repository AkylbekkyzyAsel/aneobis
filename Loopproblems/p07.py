a = input()
b = list(a)
i = 0;
q = 0
aaa = []
for num in b:
        if num not in aaa:
            aaa.append(num)
            
if (len(b) == len(aaa)): print("NO")
else: print("YES")