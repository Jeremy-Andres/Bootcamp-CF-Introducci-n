saldo_de_cuenta = 0

def evaluar_movimiento(monto_movimiento,saldo_local):
    if monto_movimiento == 0:
        print("Movimiento inválido")
    elif monto_movimiento < 0 and (monto_movimiento * -1) > saldo_local:
    #No hagas nada
        print("No tienes suficiente saldo")
    else:
        if monto_movimiento > 0:
            print("Se ha realizado un depósito")
        elif monto_movimiento < 0:
            print("Se ha realizado un retiro")
        saldo_local = saldo_local + monto_movimiento  # Ejecutar el movimiento
        return saldo_local

saldo_de_cuenta = evaluar_movimiento(1000, saldo_de_cuenta)  # Deposité 1000

saldo_de_cuenta = evaluar_movimiento(-500, saldo_de_cuenta)  # 500


print("Tu saldo final es",saldo_de_cuenta)