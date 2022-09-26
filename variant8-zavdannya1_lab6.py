#Лабароторна 6 варіант 8 завдання1. Посилання на GitHub https://github.com/Olllesssyya/Lab6
import math
a=float(input("Введіть ціле число a:"))
b=float(input("Введіть ціле число b:"))
h=float(input("Введіть ціле число h:"))
x=a
for i in range(100):
        f=math.log(math.fabs(x+pow(math.e,x)),3)
        f=round(f,4)
        #print("При x=%.3f значення функції дорівнює: %f"%(x,f))
        print (i,'x =',x,'f =',f)
        x=x+h
        x=round(x,3)
        if x>b:
            break