PASS = "Admin123"
INTENTOS_MAS = 3
pass_usuario = input("contraseña? ")
intento = 1

while pass_usuario != PASS and intento < INTENTOS_MAS:
    print("Contraseña Invalida")
    pass_usuario = input("contraseña? ")
    intento += 1

if pass_usuario == PASS:
    print("Acceso concedido")
else:
    print("Cantidad de intentos maximos alcanzados")
