#Лабароторна 6 варіант 8 завдання2. Посилання на GitHub https://github.com/Olllesssyya/Lab6
import math
a=float(input("Введіть число a:"))
b=float(input("Введіть число b:"))
h=float(input("Введіть число h:"))
x=a
i=0
while x<b:
        f=math.log(math.fabs(x+pow(math.e,x)),3)
        f=round(f,4)
        i=i+1
        print (i,'x =',x,'f =',f)
        x=x+h
        x=round(x,3)
        if x>b:
            break