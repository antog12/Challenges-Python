#20

"""nombre = input("Escribe tu nombre:")
longitud = len(nombre)
print(f"Hola {nombre}, tu nombre tiene una longitud de {longitud} caractéres")
"""
#21
"""nombre = input("Escribe tu nombre:")
apellido = input("Escribe tu apellido:")
completo = nombre + " " + apellido
print(f"Hola {completo}, tu nombre tiene una longitud de {len(completo)} letras")
"""

#22
"""nombre = input("Escribe tu nombre en minusculas:")
apellido = input("Escribe tu apellido en minusculas:")
nombre=nombre.title()
apellido=apellido.title()
completo = nombre + " " + apellido
print(completo)"""

#23

"""texto= ("En un lugar de la Mancha de cuyo nombre no quiero acordarme")
longitud=len(texto)
print(f"La longitud del texto es {longitud} caracteres.")
ini = int(input("numero inicial:"))
fin = int(input("numero final:"))
parteDelTexto = (texto[ini:fin])
print(parteDelTexto)
##OJOOOO con no sobreescribir el texto con len ya que me da un int y entonces no puedo sacar la cadena

"""

#24
"""texto= input("Escribe al y pásalo a mayúsculas:")
texto= texto.upper()
print(texto)"""

#25

"""nombre= input("Escriba su nombre:")
if len(nombre) < 5:
    apellido = input("Escriba también su apellido:")
    nombre=nombre.upper()
    print(nombre+apellido)
else:
    print(nombre.lower())"""

#26

palabra= input("introduce una palabra:")
primera= palabra[0]
longitud = len(palabra)
resto= palabra[1:longitud]
print(primera)
print(longitud)
print(resto)

if primera != "a" and primera != "e" and primera != "i" and primera != "o" and primera != "u":
    nuevaPalabra = resto + primera + "ay"
else:
    nuevaPalabra = palabra+"way"
print(nuevaPalabra.lower())












