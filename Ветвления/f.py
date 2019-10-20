a = input()
b = list(a)
q1 = int(a)
q2 = int(b[len(a) - 1])
if (q1 == 1): print("Вам 1 год.")
elif (q1 >= 2 and q1 <= 4): print("Вам", a, "года.")
elif (q1 >= 5 and q1 <= 20): print("Вам", a, "лет.")
elif (q1 >= 21):
    if (q2 == 1): print("Вам", a, "год.")
    elif (q2 >= 2 and q2 <= 4): print("Вам", a, "года.")
    elif (q2 == 0 or q2 >= 5 and q2 <= 9): print("Вам", a, "лет.")
   




