#45

"""total = 0
while total <= 50:
    num=int(input("Introduce un número:"))
    total = total + num
    print(f"el total es {total}")"""


#46
"""num= 0
while num <=5:
    num = int(input("introduce un número:"))
print(f"el último numero introducido ha sido el {num}")"""

#47

"""num1 = int(input("Introduce un número:"))
total = num1
again = "y"

while again == "y":
    num2 = int(input("Introduce otro número:"))
    total = total + num2
    again = input("Quieres introducir otro número? (y/n)")
print(f"el total es {total}")"""

#48

"""invitados= int(input("Cuántas personas quieres invitar a la fiesta?"))
total = 0
if invitados < 10:
    for i in range(0,invitados):
        ans= input("Nombre del invitado?")
        print(f"{ans} ha sido invitado")
        total = total + 1
    print(f"número de invitados: {total}")
else:
    print("demasiadas personas")"""

"""again = "y"
total = 0
while again == "y":
    ans = input("Nombre del invitado?:")
    print(f"{ans} ha sido invitado")
    total = total + 1
    again = input("Quieres invitar a alguien más? (y/n)")
print(f"número de invitados: {total}")"""

#49

"""compnum = 50
count = 1
num = int(input("Ingrese un número:"))
while num != compnum:
    if num < compnum:
        print("el número es más bajo, ingrese otro")
    else:
        print("el número es más alto, ingrese otro")
    count = count +1
    num = int(input("Ingrese otro número:"))
print(f"felicidades, lo has acertado en {count} intentos")"""

#50

"""num = int(input("Ingrese un número entre 10 y 20:"))

while num<10 or num>20:
    if num<10:
        print("demasiado bajo")
    else:
        print("demasiado alto")
    num = int(input("Ingrese un número entre 10 y 20:"))
print("Gracias")"""

#51


botellas = 10
while botellas>=0:
    print(botellas)
    botellas=botellas-1





