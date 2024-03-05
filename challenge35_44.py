#35

"""nombre=input("introduce tu nombre:")

for i in range(0,3):
    print(nombre)"""

#36

"""nombre=input("introduce tu nombre:")
num= int(input("Introduce un número:"))

for i in range(0,num):
    print(nombre)"""

#37

"""nombre=input("introduce tu nombre:")

for i in nombre:
    print(i)"""

#38

"""nombre=input("introduce tu nombre:")
num= int(input("Introduce un número:"))
for i in range(0,num):
    for i in nombre:
        print(i)"""


#39
"""num=int(input("introduzca un número entre 1 y 12"))
for i in range(0,13):
    respuesta = i * num
    print(f"{i} x {num} = {respuesta}")"""

#40

"""num= int(input("introduce un número:"))

if num < 50:
    for i in range(num,0,-1):
        print(i)
else:
    print("Has elegido un num superior a 50")"""


#41

"""nombre= input("Introduce tu nombre:")
num= int(input("introduce un número:"))

if num < 10:
    for i in range(0,num):
        print(nombre)
else:
    for i in range(0,3):
        print("Demasiado alto")"""



#42

"""total = 0
for i in range(0,5):
    num = int(input("introduce un número:"))
    ans = input("Quieres incluir este número? (y/n) ")
    if ans == "y":
        total = total + num
print(total)"""

#43

"""ans = input("En que dirección quieres contar? (u/d)")

if ans == "u":
    num=int(input("ingrese un num:"))
    for i in range(0,num):
        print(i)
elif ans == "d":
    num = int(input("ingrese un num por debajo de 20:"))
    for i in range(20,num,-1):
        print(i)"""


#44

invitados= int(input("Cuántas personas quieres invitar a la fiesta?"))
total = 0
if invitados < 10:
    for i in range(0,invitados):
        ans= input("Nombre del invitado?")
        print(f"{ans} ha sido invitado")
        total = total + 1
    print(f"número de invitados: {total}")
else:
    print("demasiadas personas")









