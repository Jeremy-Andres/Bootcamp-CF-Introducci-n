numeros = [ 5 , 2 , 1 ]

def burbuja(numeros):
    
    intercambio = True
    
    while intercambio:
        
        intercambio = False
        
        for i in range(len(numeros) - 1):
            
            print(f"{numeros[i]} > {numeros[i + 1]} = {numeros[i] > numeros[i + 1]}")
            
            if(numeros[i] > numeros[ i + 1 ]):
                
                numero0 = numeros[i]
                numero1 = numeros[i + 1]
                numeros[i] = numero1
                numeros[i + 1] = numero0
                intercambio = True
burbuja(numeros)