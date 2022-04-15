#Definimos la clase
class Alarma:   
    #Definos funciones para la clase
    def __init__(self):         #Metodo constructor
    #Definimos atributos
        self.fecha_de_alarma = "31-03-2022"

    #Definos funciones para la clase
    def programar(self):
        print("Hola soy programar")

#Creamos un objeto
alarma = Alarma()
alarma_dos = Alarma()

alarma.fecha_de_alarma = "01-04-2022"

print(alarma.fecha_de_alarma)
print(alarma_dos.fecha_de_alarma)
