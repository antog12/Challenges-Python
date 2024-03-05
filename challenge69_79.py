"""fruit_tuple = ("apple","banana","strawberry","orange")

print(fruit_tuple.index("strawberry")) #nos dice en que indice se encuentra
print(fruit_tuple[2])#nos dice el nombre en esa posición

names_list = ["John","Tim","Sam"]
del names_list[1] #elimina la posición 1
print(names_list)

names_list.append(input("añade un nombre:")) #añade a la lista
print(names_list)

names_list.sort() #ordena la lista alfabeticamente
print(names_list)

colours = {1:"red",2:"blue",3:"green"}
print(colours)

colours[2]= "yellow"
print(colours)"""

"""x = [154,634,892,345,341,43]
print(len(x))
print(x[1:4])#4 excluido

for i in x:
    print(i)

num = int(input("Introduce un número:"))
if num in x:
    print("El número está en la lista")
else:
    print("No está en la lista")

x.insert(2,420) #inserta el 420 en la posición 2
print(x)

x.remove(892)
print(x)

x.append(993)#inserta al final de la lista

print(x)"""

print("--------------------------------")
print("--------------------------------")
print("--------------------------------")

#69

"""paises = ("España", "Francia","Alemania","Italia","Portugal")
print(paises)

introduce= input("Dime un pais y te digo su posición:")
print(paises.index(introduce))"""

#70
"""paises = ("España", "Francia","Alemania","Italia","Portugal")
introduce= int(input("Dime una posición y te digo su país:"))
print(paises[introduce])"""

#71

"""deportes = ["futbol", "tenis"]
user=input("cual es tu deporte favorito?")
deportes.append(user)
deportes.sort()
print(deportes)"""

#72

"""asignaturas = ["mates","lengua","ingles","sociales","deporte","dibujo"]
eliminar=input("que asignatura no te gusta?")
asignaturas.remove(eliminar)
print(asignaturas)"""

#73

"""comidas = {1:"pizza",2:"hamburguesa",3:"sushi",4:"paella"}
print(comidas)

eliminar=int(input("que comida no te gusta?"))
del comidas[eliminar]
print(comidas)"""

#74

colores = [
    'Rojo',
    'Verde',
    'Azul',
    'Amarillo',
    'Cian',
    'Magenta',
    'Negro',
    'Blanco',
    'Gris',
    'Naranja'
]

"""print(colores)
ini= int(input("número de inicio de la lista entre 0 y 4?"))
fin = int(input("número de fin de la lista entre 5 y 9?"))

if ini < 0 or ini > 4:
    print("número incorrecto")
elif fin < 5 or fin > 9:
    print("número incorrecto")
else:
    print(colores[ini:fin])"""


#75

"""numeros= [123,456,789,699]
print("***Muestra lista separados***")
for i in numeros:
    print(i)

user = int(input("introduce un número de tres cifras"))

if user <100 or user>999:
    print("has introducido un número erróneo")
elif user in numeros:
    print(f"El número está en la posición {numeros.index(user)}")
else:
    print("no está en la lista")"""


#76

"""invitados= []
for i in range(0,3):
    añadir = input("Dime el nombre de invitado a añadir a la lista")
    invitados.append(añadir)
print(invitados)
#lo puedo hacer con len
#count= 0
pregunta = input("Quieres añadir más invitados (y/n):?")
while  pregunta == "y":
    nuevosInvitados = invitados.append(input("introduce otro nombre:"))#este es solo para introducir nuevos, tienes que mostrar la lista
    pregunta = input("Quieres añadir más invitados (y/n)?")
    print(invitados)
print(f"tienes {len(invitados)} a la fiesta")"""

#77

"""invitados= []
for i in range(0,3):
    añadir = input("Dime el nombre de invitado a añadir a la lista")
    invitados.append(añadir)
print(invitados)
#lo puedo hacer con len
#count= 0
pregunta = input("Quieres añadir más invitados (y/n):?")
while  pregunta == "y":
    nuevosInvitados = invitados.append(input("introduce otro nombre:"))#este es solo para introducir nuevos, tienes que mostrar la lista
    pregunta = input("Quieres añadir más invitados (y/n)?")
    print(invitados)
print(f"tienes {len(invitados)} a la fiesta")

print("*************")
nombre= input("teclea un nombre de la lista:")
if nombre in invitados:
    print(f"la posición de {nombre} es {invitados.index(nombre)}")
print("*************")

venir = input(f"quieres que {nombre} venga a la fiesta (y/n)?")

if venir == "y":
    print(f"{nombre} puede venir a la fiesta")
else:
    elim = invitados.remove(nombre)
print(invitados)"""

#78

"""tv = ["caza", "pesca", "coches", "cocina"]

for i in tv:
    print(i)
print("+++++++++++")
user = input("-introduce otro programa de tv:")
posición = int(input("introduce una posición:"))

tv.insert(posición,user)

for i in tv:
    print(i)
"""
#79

numeros = []

for i in range(0,3):
    añadir = int(input("Dime el numero a añadir a la lista"))
    numeros.append(añadir)
print(numeros)

print("+++++++++++++")

pregunta = input("Quieres que se guarde el último número de la lista (y/n)")

if pregunta == "y":
    print(numeros)
else:
    numeros.pop()
    print(numeros)





