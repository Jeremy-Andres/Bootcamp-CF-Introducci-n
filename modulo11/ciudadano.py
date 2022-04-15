class Ciudadano:
    def asign_nombre(self, nombres, apellido_paterno, apellido_materno):
        self.nombre_completo = nombres + apellido_paterno + apellido_materno

class CiudadanoNorteAmericano(Ciudadano):
    def asign_nombre(self, primer_nombre, primer_apellido ):
        self.nombre_completo = primer_nombre + primer_apellido      # sobreescritura de metodos

uriel = Ciudadano()
uriel.asign_nombre('Marcos Uriel', 'Hernandez', 'Camacho')
print(uriel.nombre_completo)

cody = CiudadanoNorteAmericano()
cody.asign_nombre('Cody', 'Cocodrilo')
print(cody.nombre_completo)