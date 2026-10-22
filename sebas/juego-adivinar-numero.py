"""
Ejemplo:

El programa genera un numero al azar y el usuario intentará adivinarlo.
En cada intento, el programa le dirá si el numero a adivinar es mayor o menor.
El programa se acaba cuando la persona logre adivinar el número.
El programa mostrará cuantos intentos necesito el usuario para adivinar.
Gana la persona que adivine con menos intentos.
El numero al azar está entre 0 y 1000.

"""

import random

NUM_ADIVINAR = random.randint(0, 1000)

intentos = 0
while True:
    # Leer y validar el numero del usuario
    num = 0
    while True:
        num = int(input("Intente adivinar, ingrese un numero de 0 a 1000: "))
        if 0 <= num <= 1000:
            break
        print("Error numero invalido. El rango es de 0 a 1000")
        input("Presione Enter para continuar . . .")
        print("")

    intentos += 1

    if num ==   NUM_ADIVINAR:
        break
    if num > NUM_ADIVINAR:
        input ("El numero a adivinar es menor. \nPresione Enter para continuar ...")
        print("")
    else:
        input ("El numero a adivinar es mayor. \nPresione Enter para continuar ...")
        print("")


print("Haz adivinado!!!")
print("Usaste", intentos, " intento(s).")