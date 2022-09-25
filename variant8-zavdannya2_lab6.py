#Лабароторна 6 варіант 8 завдання2. Посилання на GitHub https://github.com/Olllesssyya/Lab6
import math
a=int(input("Введіть ціле число a:"))
b=int(input("Введіть ціле число b:"))
h=float(input("Введіть h:"))
x=a
if a<b:
    while x<b:
        f=math.log(math.fabs(x+pow(math.e,x)),3)
        print("При x=%.1f значення функції дорівнює: %f"%(x,f))
        x=x+h
else:
    print("Число а повинно бути більше, чим b")