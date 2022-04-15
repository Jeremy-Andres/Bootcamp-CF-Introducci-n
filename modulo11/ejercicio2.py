class PlanCurricular:
    def __init__(self, nombre):
        self.nombre = nombre

class Bootcamp(PlanCurricular):
    def inscribir(self):
        print('Hola', self.nombre, 'bienvenido al bootcamp')

prueba = Bootcamp('Jeremy')
prueba.inscribir()