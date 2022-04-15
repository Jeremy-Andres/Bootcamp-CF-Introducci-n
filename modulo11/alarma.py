#Definimos la clase
class Alarma:
    #Definimos el método constructor
    def __init__(self,fecha_alarma, melodia):
        self.fecha_programar = fecha_alarma
        self.melodia = melodia 
        self.volumen = 0

    #Definos funciones para la clase
    def programar(self):
        print(self.fecha_programar)

    def subir_volumen(self):
        self.volumen = self.volumen + 1

    def bajar_volumen(self):
        self.volumen = self.volumen - 1

#Creamos un objeto
alarma = Alarma("04-04-2022", 'aves.mp3')

print(alarma.fecha_programar)
print(alarma.melodia)
print(alarma.volumen)