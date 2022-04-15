# 1.-Reemplaza vocales por @.
mensaje = 'Hola MUNdo' #hay que verlo como una lista de caracteres
vocales = ['a', 'e', 'i', 'o', 'u']

nuevo_mensaje = ''   #No es mutable

for caracter in mensaje:
    if caracter.lower() in vocales:   #tambien podrian hacerse 2 listas de vocales mayusculas y minusculas
        caracter = '@'

    nuevo_mensaje = nuevo_mensaje + caracter
    #print(nuevo_mensaje)
    
print(nuevo_mensaje)