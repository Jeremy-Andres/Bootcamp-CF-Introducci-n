class Vehiculo:
    def encender(self):
        print('Prendi el motor de combhustible')

class VehiculoHibrido(Vehiculo):
    def encender(self):
        print('Prendi el motor electrico')

v = VehiculoHibrido()
v.encender()    

# Salida: Prendi el motor electrico
# otra forma de sobreescritura

# si quisieramos llamar el metodo de la clase padre deberiamos usar super().enecender() 