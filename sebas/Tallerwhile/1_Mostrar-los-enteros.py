"""
Una actividad recibe dos enteros A y B con A < B. Muestre, en orden ascendente, todos los enteros
estrictamente mayores que A y menores que B. Los extremos no se muestran. Si no hay enteros entre
ellos, informe «No hay enteros interiores».

Fórmula o relación: Cada entero consecutivo difiere del anterior en 1.

"""
A = int(input("Ingrese el valor de A"))
B = int(input("Ingrese el valor de B"))

entero_entreayb = A + 1

if B == entero_entreayb:
    print("No hay enteros interiores")
while entero_entreayb < B:
    print(entero_entreayb)
    entero_entreayb+= 1
    