# Inicia con la palabra def nombre_funcion(parametros)
def evaluar_movimiento(monto_movimiento):
    # Aquí va el código
    if monto_movimiento > 0:
        print("Se ha realizado un depósito")
    elif monto_movimiento == 0:
        print("Movimiento inválido")
    elif monto_movimiento < 0:
        print("Se ha realizado un retiro")


evaluar_movimiento(0) 

saldo_de_cuenta = 0

# Primer movimiento 1000
primer_movimiento = 1000
saldo_de_cuenta += primer_movimiento # Ejecutar el movimiento
evaluar_movimiento(primer_movimiento) # Llamar a la funcion monto_movimiento = 1000

# Segundo movimiento 400
segundo_movimiento = 400
saldo_de_cuenta += segundo_movimiento # Ejecutar el movimiento
evaluar_movimiento(segundo_movimiento) # Llamar a la función moto_movimiento = 400

# Tercer movimiento -100
tercer_movimiento = -100

saldo_de_cuenta += tercer_movimiento # Ejecutar el movimiento
evaluar_movimiento(tercer_movimiento)

# Cuarto movimiento -500
cuarto_movimiento = -500

saldo_de_cuenta += cuarto_movimiento # Ejecutar el movimiento
evaluar_movimiento(cuarto_movimiento)

#Quinto movimiento 300
quinto_movimiento = 300

saldo_de_cuenta += quinto_movimiento # Ejecutar el movimiento
evaluar_movimiento(quinto_movimiento)

print(saldo_de_cuenta)