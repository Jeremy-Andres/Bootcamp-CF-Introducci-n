saldo_de_cuenta = 0

def evaluar_movimiento(monto_movimiento):
    global saldo_de_cuenta # Lo explicaremos más tarde

    if monto_movimiento == 0:
        print("Movimiento inválido")
        return
    elif monto_movimiento < 0 and (monto_movimiento * -1) > saldo_de_cuenta:
    #No hagas nada
        print("No tienes suficiente saldo")
        return

    if monto_movimiento > 0:
        print("Se ha realizado un depósito")
    elif monto_movimiento < 0:
        print("Se ha realizado un retiro")

evaluar_movimiento(-500)