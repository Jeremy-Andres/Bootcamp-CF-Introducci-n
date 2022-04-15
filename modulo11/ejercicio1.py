class Usuario:            # la clase no lleva ()
    def __init__(self):
        self.nombre = 'Jeremy'

    def presentarse(self):
        print('Hola soy', self.nombre)
        #return self.nombre

    def asignar_apodo(self, apodo):
        self.nombre = apodo

jeremy = Usuario()              

jeremy.presentarse()                       #los metodos llevan () al final
#print('Hola soy', jeremy.presentarse()) 

jeremy.asignar_apodo('Jere')      
print('Mi apodo es', jeremy.nombre)  
