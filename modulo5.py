def validarFloat(mensaje):
    while True:
        try:
            data = float(input("Coloca " + mensaje +": "))
            return data;
        except ValueError:
            print("El dato debe ser un valor entero o decimal")


producto = input("¿Qué compraras? ")
precio = validarFloat(" el precio de lo que compraras ")
ahorroActual = 0

while precio > ahorroActual:
    mesada = validarFloat(" tu mesada ")
    ahorroActual = ahorroActual + mesada
    restante = precio - ahorroActual

    tiempoTotal = precio / mesada
    tiempoActual = ahorroActual / mesada
    tiempoRestante = tiempoTotal - tiempoActual

    print("Actualmente llevas ahorrado ", ahorroActual)
    print("El dinero que te falta es $", restante)
    print("Lo meses que te faltan para cumplir tu meta son", tiempoRestante)

print("Felicidades llegaste a tu meta ya puedes comprar ", producto)
