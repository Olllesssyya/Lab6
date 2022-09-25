#Лабароторна 6 варіант 8 завдання3. Посилання на GitHub https://github.com/Olllesssyya/Lab6
import math
a=int(input("Введіть ціле число a:"))
b=int(input("Введіть ціле число b:"))
h=float(input("Введіть h:"))
spisok=[]
x=a
if a<b:
    while x<b:
        f=math.log(math.fabs(x+pow(math.e,x)),3)
        spisok.append(f)
        x=x+h
else:
    print("Число а повинно бути більше, чим b")
print(*spisok, sep="\n")
