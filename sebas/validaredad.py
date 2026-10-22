"""
Ejemplo:

hacer un programa que lea una edad y continue si esta es valida.

Una edad valida es: 16 <= edad_camper <= 40
"""

edad = int(input("Edad? "))
while True:
    if edad < 16 or edad > 40:
        print("Error, Edad invalida. Vuelva a ingresarla [16, 40].")
        input("Presione cualquier tecla para continuar . . .")
        edad = int(input("Edad? "))
    else:
        print("La edad es correcta,")
        break