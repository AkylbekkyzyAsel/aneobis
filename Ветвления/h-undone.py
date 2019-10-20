a = input()
b = a.split(" ")
d = int(b[0])
m = int(b[1])
r = 0
if(m == 1):
    r = d % 7 + 4
elif(m == 2):
    r = d % 7
elif(m == 3):
    r = d % 7 + 1
elif(m == 4):
    r = d % 7 + 4
elif(m == 5):
    r = d % 7 + 6
elif(m == 6):
    r = d % 7 + 2
elif(m == 7):
    r = d % 7 + 4
elif(m == 8):
    r = d % 7
elif(m == 9):
    r = d % 7 + 3
elif(m == 10):
    r = d % 7 + 5
elif(m == 11):
    r = d % 7 + 1
elif(m == 12):
    r = d % 7 + 3 
while(r > 7):
        r = r % 7


if(r == 1): print("Monday")
elif(r == 2): print("Tuesday")
elif(r == 3): print("Wednesday")
elif(r == 4): print("Thursday")
elif(r == 5): print("Friday")
elif(r == 6): print("Saturday")
elif(r == 7): print("Sunday")

