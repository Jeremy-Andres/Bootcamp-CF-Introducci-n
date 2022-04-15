from random import randint

def adivina_numero(): #parametros + Variables dentro de los ()
    numero_secreto = randint(0, 100)

    ganador = False
    
    for intento in range(0, 5):
        numero_pensando = input('En que numero estoy pensando? ')
        numero_pensando = int(numero_pensando)

        if numero_pensando == numero_secreto:
            ganador = True
            print('Felicidades, el numero es correcto')
            break
        else:
            if numero_pensando < numero_secreto:
                print('Mas alto.')
            else:
                print('Mas bajo')

    if ganador == False:
        print('El numero secreto es:' + str(numero_secreto))

    print('Gracias por jugar')

adivina_numero()