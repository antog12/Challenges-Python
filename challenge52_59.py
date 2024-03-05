import random

#52

"""num = random.randint(0,100)
print(num)"""

#53

"""frutas =  ["banana", "melon", "naranja", "uva", "pera"]
elegir = random.choice(frutas)
print(elegir)"""

#54

"""jugar = ["cara","cruz"]
elegir = random.choice(jugar)

preguntar= input("elige cara o cruz")

if preguntar == elegir:
    print("ganas")
else:
    print("mala suerte")
if elegir == "cara":
    print("fue cara")
else:
    print("fue cruz")"""

#55

"""num = random.randint(1,5)
user= int(input("Introduce un número:"))

if user == num:
    print("Bien hecho")
elif user>num:
    print("demasiado alto")
    user = int(input("Introduce otro número:"))
    if user == num:
        print("correcto")
    else:
        print("Tu pierdes")
elif user<num:
    print("demasiado bajo")
    user = int(input("Introduce otro número:"))
    if user == num:
        print("correcto")
    else:
        print("Tu pierdes")"""



#56
"""count = 1
num = random.randint(1,10)
user= int(input("Introduce un número:"))

while num != user:
    user = int(input("Introduce un número:"))
    count = count + 1
print(f"feliocidades,tu num era el {user} y el aleatorio era el {num}\n y lo has acertado a la {count}")"""

#57
"""count = 1
num = random.randint(1,10)
user= int(input("Introduce un número:"))

while num != user:
    if user > num:
        print("demasiado alto")
        user = int(input("Introduce otro número:"))
    elif user < num:
        print("demasiado bajo")
        user = int(input("Introduce otro número:"))
    count = count + 1
print(f"feliocidades,tu num era el {user} y el aleatorio era el {num}\n y lo has acertado a la {count}")"""

#58


"""score = 0
for i in range(1,6):
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    suma= num1 + num2
    print(f"{num1} + {num2} =")
    respuesta = int(input("Introduce respuesta:"))
    print()
    if respuesta == suma:
        score = score +1
print(f"Tu puntuación ha sido {score} de 5")"""


#59
count = 1
colores = ["azul","verde","negro","amarillo","rosa"]
colores= random.choice(colores)
print(colores)
user = input("elige un color:")
if colores == user:
    print("bien hecho")
while colores!=user:
    print(f"Apouesto a que estas {colores} de envidia")
    user = input("elige otro color:")
    count = count +1
print(f"feliocidades,tu color era el {user} y el aleatorio era el {colores}\n y lo has acertado a la {count}")











