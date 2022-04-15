def saludo():   ##saludo y opciones de medidas
    print("Hola! Este es un programa que convierte unidades de medida del Sistema internacional al Sistema inglés\n"
    " 1. Longitud\n 2. Masa\n 3. Volumen \n Ingresa el número de la opción que quieras seleccionar:")

def longi():  ##función para unidades de longitud
    metros = float(input("Ingresa la unidad en metros: "))
    inc = round(metros / 0.0254, 3)
    pie = round(metros / 0.3048, 3)
    yd = round(metros / 0.914, 3)
    mill = round(metros / 1.609, 3)

    print(metros, " metros equivale a:\n" , inc , " pulgadas,\n" ,pie , " pies,\n" ,yd , " yardas,\n" ,mill , " millas.")


def masa(): ##función para unidades de masa
    gramos = float(input("Ingrese la unidad en gramos: "))
    lb = round(gramos / 453.6, 3)
    oz = round(gramos / 28.35, 3)
    ton = round(gramos / 907.2, 3)

    print(gramos, " gramos equivale a:\n" , lb , "libras,\n" , oz , "onzas,\n" , ton , "toneladas.")

def vol():  #función para unidades de volumen
    ltr = float(input("Ingrese la cantidad en litros: "))
    gal = round(ltr / 3.785, 3)
    qt = round(ltr / 946.4, 3)
    piecub = round(ltr / 28.32, 3)

    print(ltr, "litros es equivalente a:\n" , gal , "galones,\n" , qt , "cuartos,\n" , piecub, "pies cubicos.")

def alt(): #función para escoger una alternativa
    resp = int(input())
    if resp == 1:
        longi() 
    elif resp == 2:
        masa()
    elif resp == 3:
        vol()
    else:
        print("Respuesta incorrecta\n")
        saludo()
        alt()

saludo()
alt()



