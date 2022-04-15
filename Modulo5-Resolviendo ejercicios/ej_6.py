numero = input('Ingrese un numero: ')

def cantidad_digitos(num):
    digitos = 0
    for d in num:
        digitos = digitos + 1
        return digitos
    
    print(digitos)


cantidad_digitos(numero)

