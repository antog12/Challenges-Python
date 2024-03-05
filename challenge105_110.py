#105
"""archivo = open("Numeros.txt","w")
archivo.write("1, ")
archivo.write("2, ")
archivo.write("3, ")
archivo.write("4, ")
archivo.write("5, ")
archivo.close()"""

#106

"""archivo = open("Nombre.txt","w")
archivo.write("Anto\n")
archivo.write("Josemi\n")
archivo.write("Paula\n")
archivo.write("Candela\n")
archivo.write("Cheto\n")
archivo.close()"""

#107

"""archivo = open("Nombre.txt","r")
print(archivo.read())"""

#108

"""archivo = open("Nombre.txt","a")
user = input("introduce un nombre nuevo:")
archivo.write(user+"\n")
archivo.close()
archivo = open("Nombre.txt","r")
print(archivo.read())"""

#109

"""print("*********")
print("1) Crea un nuevo archivo.")
print("2) Muestra el archivo por pantalla.")
print("3) añade un nuevo objeto al archivo:")
print("*********")

elegir = int(input("Selecciona 1, 2 o 3:"))

if elegir == 1:
    archivo = open("animales.txt", "w")
    user = input("introduce un animal nuevo:")
    archivo.write(user + "\n")
    user = input("quieres introducir otro animal (y/n)?")
    while user == "y":
        user = input("introduce un animal nuevo:")
        archivo.write(user + "\n")
        user = input("quieres introducir otro animal (y/n)?")
    archivo.close()
elif elegir == 2:
    archivo = open("animales.txt", "r")
    print(archivo.read())
elif elegir == 3:
    archivo = open("animales.txt","a")
    user = input("introduce un animal nuevo:")
    archivo.write(user+"\n")
    archivo.close()
else:
    print("opción inválida")"""

#110

archivo= open("Nombre.txt","r")
print(archivo.read())
archivo.close()

archivo= open("Nombre.txt","r")
selectedName= input("Introduce un nombre de la lista:")
selectedName = selectedName + "\n"
for row in archivo:
    if row != selectedName:
        archivo = open("Nombre2.txt","a")
        newrecord = row
        archivo.write(newrecord)
        archivo.close()
archivo.close()











