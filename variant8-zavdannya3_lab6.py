#Лабароторна 6 варіант 8 завдання3. Посилання на GitHub https://github.com/Olllesssyya/Lab6
import math
a=int(input("Введіть ціле число a:"))
b=int(input("Введіть ціле число b:"))
h=float(input("Введіть h:"))
spisok=[]
x=a
while x<b:
    f=math.log(math.fabs(x+pow(math.e,x)),3)
    f=round(f,4)
    spisok.append(f)
    x=x+h
    x=round(x,3)
    if x>b:
        break
print(*spisok, sep="\n")
