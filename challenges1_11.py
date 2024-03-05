#1
print("Hello, Anto")
#2
print("Hola Anto Abellán")
#3
print("Como llamas a un oso que no tiene dientes?\nUn gummy bear")
#4
print("introduce dos números:")
num1=int(input())
num2=int(input())
print(f"los numeros introducidos son el {num1} y el {num2}")
#5
print("introduce 3 números:")
num1=int(input())
num2=int(input())
num3=int(input())
print((num1+num2)*num3)
#6
print("Cuantas porciones de pizza hay?")
porciones=int(input())
print(f"En la caja hay {porciones} porciones")
print("Cuantas te has comido?")
comido=int(input())
print(f"Me he comido {comido} porciones")
print("Cuantas porciones quedan en la caja?")
resultado=porciones-comido
print(f"quedan {resultado} porciones")
#7
print("Nombre:")
nombre=input()
print("Edad:")
edad=int(input())
nueva_edad = edad + 1
print(f"{nombre},el año que viene tendrás {nueva_edad} años")

#8
print("Precio de la cuenta?:")
cuenta=float(input())
print("Número de comensales?")
comensales=int(input())
total=cuenta/comensales
print(f"tocamos a {total} euros por persona")
#9
dias= int(input("Ingrse el número de días:"))
horas=dias*24
minutos=horas*60
segundos=minutos*60
print(f"En {dias} dias, hay ,{horas} horas, {minutos} minutos, {segundos} segundos ")

#10
un_kilo= 2.204
print("Convertir kilos a libras")
kilos=int(input("Ingrese los kilos a convertir"))
print("Convirtiendo a libras...")
total= kilos*un_kilo
print(f"{kilos} kilos son {total} libras")
#11
num_largo=int(input("Ingrese un número por encima de 100:"))
num_bajo=int(input("Ingrese un número por debajo de 10:"))
respuesta=num_largo/num_bajo
print(f"{num_bajo} se repite en {num_largo}, {respuesta} veces")









