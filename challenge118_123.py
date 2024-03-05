#funciones
"""
def get_name():
    user_name = input("Introduce tu nombre:")
    return user_name

def print_mag(user_name):
    print("Hola",user_name)

def main():
    user_name = get_name()
    print_mag(user_name)

main()"""
#--------------------------
def get_data():
    userName= input("introduce tu nombre:")
    age= int(input("introduce tue edad"))
    dataTupla= (userName,age)
    return dataTupla

#print(get_data())
#-----------------------------------
"""def mensaje(userName,age):
    if age <= 10:
        print("hola",userName)
    else:
        print("Hello", userName)

#mensaje("anto",9)

#-------------------------------------

def main():
    userName, age = get_data()
    mensaje(userName,age)

main()"""

#-----------------------------------------

#118

"""def preguntarNum():
    num = int(input("ingrese un número"))
    return num

#print(preguntarNum())
def contar(num):
    for i in range(0,num):
        print(i)

def main():
    num = preguntarNum()
    contar(num)

main()"""

#119
import random


# que elija un num al azar entre los dos que le pongo
"""def pregNum():
    ask1 = int(input("elije un número:"))
    ask2 = int(input("elije un número:"))
    comp_num = random.randint(ask1, ask2)
    return comp_num"""


"""def adivinanza():
    print("Estoy pensando en un número...")
    adivinar = int(input("En que número estoy pensando?:"))
    return adivinar


def chekNum(comp_num, adivinar):
    tryAgain = True
    while tryAgain == True:
        if comp_num == adivinar:
            print("correcto, tu ganas!!")
            tryAgain = False
        elif comp_num > adivinar:
            adivinar = int(input("Demasiado bajo, introduce otro num"))
        else:
            adivinar = int(input("Demasiado alto, introduce otro num"))


def main():
    comp_num = pregNum()
    adivinar = adivinanza()
    chekNum(comp_num, adivinar)


main()"""


#120

"""def suma():

    num1 = random.randint(5,20)
    num2 = random.randint(5,20)
    print(num1, "+", num2, "=")
    miRespuesta = int(input("La respuesta es:"))
    respuesta = num1 + num2
    respuestaActual = (respuesta,miRespuesta)
    return respuestaActual

def resta():
    num1 = random.randint(25, 50)
    num2 = random.randint(1, 25)
    print(num1, "-", num2, "=")
    miRespuesta = int(input("La respuesta es:"))
    respuesta = num1 - num2
    respuestaActual = (respuesta, miRespuesta)
    return respuestaActual

def chequearRespuesta(miRespuesta,respuesta):
    if miRespuesta == respuesta:
        print("correcto")
    else:
        print(f"Incorrecto, la respuesta correcta es {respuesta}")

def main():
    print("1) Sumar")
    print("2) Restar")
    seleccion = int(input("elige una opción:"))
    if seleccion == 1:
        miRespuesta,respuesta = suma()
        chequearRespuesta(miRespuesta,respuesta)
    elif seleccion == 2:
        miRespuesta, respuesta = resta()
        chequearRespuesta(miRespuesta, respuesta)
    else:
        print("Escoge entre 1 y 2")

main()"""

#121

#añadir un nombre a la lista
"""nombres = ["Juan","Alba","Pedro" ]
def insertar():
    añadir = input("Introduce un nombre para añadir:")
    nombres.append(añadir)
    return nombres


#cambiar un nombre de la lista
def cambiarNombre():

    num = 0 # es el índice
    for x in nombres:
        print(num, x)
        num = num + 1
    selectNumber = int(input("Introduce el número a cambiar:"))  # es como buscar por índice
    name = input(("introduce un nuevo nombre:"))
    nombres[selectNumber] = name
    return name

#borrar un nombre de la lista

def eliminar():
    num = 0  # es el índice
    for x in nombres:
        print(num, x)
        num = num + 1
    eliminar = int(input("que número deseas eliminar?"))
    del nombres[eliminar]
    return nombres

#mostrar todo
def mostrarTodo():
    for i in nombres:
        print(i)



def main():
    again = "y"
    while again =="y":
        print("1) añadir nombre")
        print("2) cambiar nombre")
        print("3) eliminar nombre")
        print("4 )mostrar todo")
        seleccion = int(input("Elige un número de la lista de opciones:"))
        if seleccion ==1:
            nombres = insertar() # acuerdate que lo haces todo sobre la lista!!!
        elif seleccion ==2:
            nombres = cambiarNombre()
        elif seleccion == 3:
            nombres=eliminar()
        elif seleccion ==4:
            nombres = mostrarTodo()
        elif seleccion == 5:
            again = "n"
        else:
            print("Opción incorrecta:")
        data= (nombres,again)

main()
print(nombres)"""


#122
import csv
"""
1 primero hago las funciones
2 después creo el menú
"""
"""
permítele añadir a un archivo
llamado Salarios.csv que almacenará su nombre
y su salario
"""
def añadirArchivo():
    archivo = open("Salarios.csv", "a")
    nombre = input("introduce tu nombre:")
    salarioInt = int(input("Introduce tu salario:"))
    salarioEnt = str(salarioInt)
    nuevoRegistro = nombre + "," + salarioEnt + "\n"
    archivo.write(nuevoRegistro)
    archivo.close()


"""
debería mostrar todos
registros del archivo Salarios.csv
"""
def mostrarArchivos():
    archivo = open("Salarios.csv", "r")
    for fila in archivo:
        print(fila)
    archivo.close()


def eliminar():
    archivo = open("Salarios.csv","r")
    x = 0
    temporal = []
    for fila in archivo: # lo paso a una lista temporal para modificar el csv
        temporal.append(fila)
    archivo.close()
    print("--------")
    for fila in temporal:
        display = x, temporal[x]  # mostraría esto (1, ['Pedro', '1000']) en su índice
        print(display)
        x = x + 1  # me da un indice para cada fila
    eliminarRegistro = int(input("Introduce el número de fila a eliminar:"))
    del temporal[eliminarRegistro]
    archivo = open("Salarios.csv", "w")
    for fila in temporal:
        archivo.write(fila)
    archivo.close()

#al seleccionar 3 se sale del programa

again = "y"
while again == "y":
    print("1) añadir archivo")
    print("2) mostrar registros")
    print("3) eliminar registros")
    print("4) salir del programa")
    print()# es comoun espacio
    seleccion = int(input("Elige un número de la lista de opciones:"))
    print()  # es comoun espacio
    if seleccion == 1:
        añadirArchivo()
    elif seleccion == 2 :
        mostrarArchivos()
    elif seleccion == 3:
        eliminar()
    elif seleccion == 4:
        again = "n"
        print("programa finalizado")
    else:
        print("Opción incorrecta, elige otra opciÓn")
    print()






