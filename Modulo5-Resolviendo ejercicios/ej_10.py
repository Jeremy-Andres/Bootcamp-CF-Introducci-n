palabra = 'Python'

nueva_palabra = ''
primer_caracter = palabra[0]

if primer_caracter.lower() in 'aeiou':  #tambien podria ser 'aeiouAEIOU'
    nueva_palabra = palabra + 'way'
else:
    nueva_palabra = palabra[1:] + primer_caracter + 'ay'


print(nueva_palabra)

