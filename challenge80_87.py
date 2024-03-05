import math
#80
"""nombre= input("Introduce tu nombre:")
lonNom= len(nombre)
print(lonNom)
print("+++++++++++")
apellido = input("Introduce tu apellido:")
lonApe= len(apellido)
print(lonApe)
print("+++++++++++")
unir= nombre + " " + apellido
lonUnir = len(unir)
print(unir)
print(lonUnir)
print("+++++++++++")"""

#81
#se hace con for
"""user = input("Introduce el nombre de tu asig favorita:")
for i in user:
    print(i, end="-")"""

#82

"""texto = "En un lugar de la Mancha de cuyo nombre no quiero acordarme"
ini= int(input("número de inicio de la lista?"))
fin = int(input("número de fin de la lista?"))
print(texto[ini:fin])"""

#83

"""texto=input("Escribe una palabra en mayúsculas")

while not texto.isupper():
    texto = input("Escribe una palabra en mayúsculas")
else:
    print(texto)"""

#84

"""postcode= input("introduce tu código postal")
start = postcode[0:2]
print(start.upper())"""

#85
"""nombre = input("Di tu nombre")
count = 0
nombre=nombre.lower()

for x in nombre:
    if x=="a" or x=="e" or x=="i" or x=="o" or x=="u":
        count = count + 1
print(f"número de vocales en el nombre:{count}")"""

#86

"""pass1 = input("Ingresa una contraseña:")
pass2 = input("Ingresa de nuevo la contraseña")

if pass1 == pass2:
    print("Gracias")
elif pass1.lower() == pass2.lower():
    print("Deben estar en el mismo caso")
elif pass1.upper() == pass2.upper():
    print("Deben estar en el mismo caso")
elif pass1 != pass2:
    print("incorrecto")"""


#87

palabra = input("introduce una palabra:")
longitud=len(palabra)
num = 1
for i in palabra:
    posicion = longitud-num
    letra = palabra[posicion]
    print(letra)
    num = num +1











