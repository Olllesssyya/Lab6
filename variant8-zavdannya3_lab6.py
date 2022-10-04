#Лабароторна 6 варіант 8 завдання3. Посилання на GitHub https://github.com/Olllesssyya/Lab6
import math
a=float(input("Введіть число a:"))
b=float(input("Введіть число b:"))
h=float(input("Введіть число h:"))
spisok=[]
x=a
while x<b:
    f=math.log(math.fabs(x+pow(math.e,x)),3)
    f=round(f,4)
    spisok.append(f)
    x=x+h
    x=round(x,3)
print(*spisok, sep="\n")
