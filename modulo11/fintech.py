class Cuenta:
    def __init__(self,saldo):
        self.saldo = saldo
        
    def evaluar_movimiento(self, monto_movimiento):
        if monto_movimiento == 0:
            print("Movimiento inválido")    
        elif monto_movimiento < 0 and (monto_movimiento * -1) > self.saldo:
            #No hagas nada
            print("No tienes suficiente saldo")
        else:
            if monto_movimiento > 0:
                print("Se ha realizado un depósito")
            elif monto_movimiento < 0:
                print("Se ha realizado un retiro")
                self.saldo = self.saldo + monto_movimiento  # Ejecutar el movimiento

cuenta_uriel = Cuenta(0)
cuenta_cody = Cuenta(100)

cuenta_uriel.evaluar_movimiento(50)

print(cuenta_uriel.saldo)
print(cuenta_cody.saldo)




