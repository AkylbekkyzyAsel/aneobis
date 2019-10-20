a = input()
b = int(a)
if(b < 0 or b > 12):
    print("Wrong number")
elif (b >= 3 and b <= 5): print("Spring")
elif (b >= 6 and b <= 8): print("Summer")
elif (b >= 9 and b <= 11): print("Autumn")
else: print("Winter")    
