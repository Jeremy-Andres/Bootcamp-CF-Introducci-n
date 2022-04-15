class Usuario:            
    def __init__(self):
        self.nombre = 'Uriel'

    def presentarse(self):
        print('Hola soy', self.nombre)

    def asignar_apodo(self, apodo):
        self.nombre = apodo

class Tutor(Usuario):       # tutor hereda de Usuario
    def asignar_clase(self, nombre_clase):
        self.clase = nombre_clase

    def iniciar_clase(self):
        print('Hoy empieza la clase', self.clase)

uriel = Tutor()
print(uriel.nombre)


