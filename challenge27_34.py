import math
#27

"""num = float(input("introduce un num con decimales:"))
resultado=num*2
print(resultado)"""

#28

"""num = float(input("introduce un num con decimales:"))
resultado=num*2
print(round(resultado,2))"""

#29
"""num = int(input("introduce un numero mayor a 500:"))

if num > 500:
    print(math.sqrt(num))
else:
    print("el numero no es mayor a 500")"""


#30

"""print(round(math.pi,5))
"""
#31

"""radio=float(input("introduce el radio de un circulo:"))
area=math.pi*radio**2
print(round(area,2))"""
#32

#volumen total es area * profundidad
"""radio=float(input("introduce el radio de un circulo:"))
profundidad= float(input("profundidad del cilindro:"))
area=math.pi*radio**2

volTotal=area*profundidad
print(volTotal)"""

#33

"""num1=int(input("Introduce un num:"))
num2= int(input("Introduce otro num:"))
division = num1//num2
resto=num1%num2

print(f"{num1} dividivo por {num2} es {division} con {resto} restante")
"""
#34
print("************")
print("1) Cuadrado\n2) Triangulo")
print("************")

num= int(input("Introduce un número:"))

if num == 1:
    lado=int(input("longitud de un lado?"))
    area=lado*lado
    print(f"el área del cuadrado es {area}")
elif num == 2:
    base = int(input("Introduce un número:"))
    altura = int(input("Introduce otro número:"))
    area= (base*altura)/2
    print(f"el área del triángulo es {area}")
else:
    print("error, elige un num correcto")
