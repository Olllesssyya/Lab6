#Лабароторна 6 варіант 8 завдання1. Посилання на GitHub https://github.com/Olllesssyya/Lab6
import math
x=0.0
a=int(input("Введіть ціле число a:"))
b=int(input("Введіть ціле число b:"))
h=int(input("Введіть ціле число h:"))
if a<b:
    for x in range(a,b,h):
        f=math.log(math.fabs(x+pow(math.e,x)),3)
        print("При x=%.1f значення функції дорівнює: %f"%(x,f))
else:
    print("Число а повинно бути більше, чим b")