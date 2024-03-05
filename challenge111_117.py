import csv

"""archivo = open("Stars.csv","w")
nuevoRegistro = "Brian,73,Tauro\n"
archivo.write(str(nuevoRegistro))
archivo.close()"""

#print("-------------------------------")

"""archivo = open("Stars.csv", "a")
nombre = input("introduce un nombre:")
edadInt = int(input("introduce tu edad:"))
edadEnt = str(edadInt)
signo = input("Introduce tu signo del zodiaco:")
nuevoRegistro = nombre + "," + edadEnt + "," + signo + "\n"
archivo.write(str(nuevoRegistro))
archivo.close()"""

#print("-------------------------------")

"""archivo = open("Stars.csv", "r")
for fila in archivo:
    print(fila)"""

#print("-------------------------------")
#leer sólo una fila
"""archivo = open("Stars.csv", "r")
leer= csv.reader(archivo)
fila = list(leer) # los meto en una lista
print(fila)
print(fila[1])# leo la fila 1"""

#print("-------------------------------")
#buscar texto en un archivo csv
"""archivo = open("Stars.csv", "r")
buscar = input("introduce el dato a buscar:")
leer= csv.reader(archivo)
for fila in archivo:
    if buscar in str(fila):
        print(fila)"""

#print("-------------------------------")
"""Un archivo .csv no puede modificarse, sólo añadirse.
Si necesita modificar el archivo debe
escribirlo en una lista temporal.
Este bloque de código leerá el archivo .csv original
y lo escribirá
a una lista llamada "tmp". 
Esta puede ser usada y alterada como una lista (ver página 58)."""

"""archivo = list(csv.reader(open("Stars.csv")))
print(archivo)
temporal = [] # esta si que puede ser modificada

for fila in archivo:
    temporal.append(fila)
print(temporal)"""
#continua abajo

#print("-------------------------------")
"""Escribe de una lista a un nuevo archivo .csv
llamado "NewStars.csv"."""

"""archivo = open("NewStars.csv", "w")
x = 0
for fila in temporal:
    nuevoRegistro =temporal[x][0] + "," + temporal[x][1] + "," + temporal[x][2] + "\n"
    archivo.write(nuevoRegistro)
    x = x +1
archivo.close()"""
"""
es muy buena práctica usar el with open ya que cierra automáticamente
el archivo incluso si hay fallos.
Ejemplo:
with open("text.txt","w") as file:
    file.write("I am learning Python!\n")
    file.write("I am really enjoying it!\n")
    file.write("And I want to add more lines to say how much I like it")


"""
"""print("-------------------------------")
print("-------------------------------")
print("-------------------------------")"""

#111

"""archivo = open("Books.csv","w")
nuevoRegistro = "To a kill a Mockingbird,Harper Lee,1960\n"
nuevoRegistro1 = "A brief history of time,Stephen Hawking,1988\n"
nuevoRegistro2 = "The great Gatsby,F. Scott Fitzgerald,1922\n"
nuevoRegistro3 = "Pride and Prejudice,Jane Austen,1813\n"
nuevoRegistro4 = "The man who mistook his wifw for a hat,Oliver Sacks,1985\n"
archivo.write(str(nuevoRegistro))
archivo.write(str(nuevoRegistro1))
archivo.write(str(nuevoRegistro2))
archivo.write(str(nuevoRegistro3))
archivo.write(str(nuevoRegistro4))
archivo.close()"""


#112

"""archivo = open("Books.csv","a")
nuevoRegistro = "The Lord of the Rings,J.R.R:Tolkien,1954\n"
archivo.write(str(nuevoRegistro))
archivo.close()

archivo = open("Books.csv","r")

for fila in archivo:
    print(fila)"""

#113

"""archivo = open("Books.csv", "a")
print("***Introduce datos***")
libros = int(input("Cuántos libros quieres ingresar:"))
if libros != 0:

    for libro in range(0, libros):
        titulo = input("introduce un titulo:")
        autor = input("Introduce el autor:")
        año = int(input("introduce el año en que se escribió:"))
        añoEnt = str(año)
        nuevoRegistro = titulo + "," + autor + "," + añoEnt + "\n"
        archivo.write(str(nuevoRegistro))
    archivo.close()
else:
    print("No hay datos para introducir.")

#vamos a buscar el autor

archivo = open("Books.csv", "r")
count = 0
buscar = input("introduce el autor a buscar:")
#leer= csv.reader(archivo)
for fila in archivo:
    if buscar in str(fila):
        print(fila)
        count = count + 1
if count == 0:
    print("No hay libros de este autor en la lista")
archivo.close()"""

#114


"""añoIni= int(input("Ingrese año de inicio de busqueda:"))
añoIniEnt = str(añoIni)
añoFin= int(input("Ingrese año de fin de busqueda:"))
añoFinEnt = str(añoFin)

archivo = list(csv.reader(open("Books.csv")))
temporal = []
for fila in archivo:
    temporal.append(fila)

x=0#puedo entender que x es cada línea de registro
for fila in temporal:
# +++IMPORTANTE, AQUI VEMOS UN DIFERENCIA ENTRE DOS FECHAS+++
    if temporal[x][2] >= añoIniEnt and temporal[x][2] <= añoFinEnt:
        print(temporal[x])
    x = x +1"""


#115

"""archivo = open("Books.csv","r")
count = 0
for fila in archivo:
    count = count +1
    print(f"fila {count} = {fila}")"""


#116

"""archivo = list(csv.reader(open("Books.csv")))
count = 0
temporal = []
for fila in archivo:
    temporal.append(fila)
print("-------------")
x = 0
for fila in temporal:
    display = x,temporal[x] #mostraría esto (1, ['A brief history of time', 'Stephen Hawking', '1988'])
    print(display)
    x = x + 1 # me da un indice para cada fila
getrid = int(input("Introduce el número de fila a eliminar:"))
del temporal[getrid]
print("-------------")
x = 0
for fila in temporal:
    display = x,temporal[x] #mostraría esto (1, ['A brief history of time', 'Stephen Hawking', '1988'])
    print(display)
    x = x + 1 # me da un indice para cada fila
alter = int(input("Introduce el número de fila a modificar:"))
x = 0
for fila in temporal[alter]:
    display = x,temporal[alter][x] #mostraría esto (1, ['A brief history of time', 'Stephen Hawking', '1988'])
    print(display)
    x = x + 1

part= int(input("que parte quieres cambiar?"))
newData = input("introduce el nuevo dato:")
temporal[alter][part] = newData
print(temporal[alter])

archivo = open(r"Books.csv", "w")
x = 0
for fila in temporal:
    newRecord = temporal[x][0] + "," + temporal[x][1] + "," + temporal[x][2] + "\n"
    archivo.write(newRecord)
    x = x + 1
archivo.close()"""

#117

import  random

print("***Math Quiz***")
score = 0
nombre = input("Introduce tu nombre:")
num1 = random.randint(1,10)
num2 = random.randint(1,10)
pregunta1 = str(num1) + " + " + str(num2) + " = "
respuesta1 = int(input(pregunta1))
realRespuesta1 = num1 + num2
if respuesta1 == realRespuesta1:
    score = score + 1

pregunta2 = str(num1) + " * " + str(num2) + " = "
respuesta2 = int(input(pregunta2))
realRespuesta2 = num1 * num2
if respuesta2 == realRespuesta2:
    score = score + 1

archivo = open ("cuestionario.csv","a")
nuevoRegistro = nombre + "," + str(pregunta1) + "," + str(respuesta1) + "," + str(pregunta2) + "," + str(respuesta2) + "," + str(score) + "\n"
archivo.write(nuevoRegistro)
archivo.close()




