"""
Un curso recibe notas entre 0 y 100, una a una, hasta recibir -99.
Muestre la cantidad de notas y su promedio.
El centinela no es una nota y no participa en el cálculo.
Si aparece primero, muestre cantidad cero y «Sin notas» en lugar de un promedio.
El flujo siempre contiene -99.
El promedio es la suma de las notas aceptadas dividida entre su cantidad.
"""

suma = 0
cantidad = 0
while True:
    while True:
        num = int(input("Ingresa las notas"))
        if 0 <= num <= 100 or num == -99:
            break
        print("Nota invalida, digite nuevamente.....")
    if num == -99:
        break
    cantidad += 1
    suma += num
if cantidad == 0:
    print("Cantidad de notas: 0; Sin notas")
else:
    prom = suma / cantidad
    print("Cantidad: ", cantidad, "; Promedio:", prom)

