class Persona:
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
    
    def hablar(self):
        print(f"{self.nombre} está hablando.")
        
class Artista:
    def __init__(self, habilidad):
        self.habilidad = habilidad

    def mostrar_habilidades(self):
        # print(f"Las habilidades de {self.nombre} son: {', '.join(self.habilidades)}")
        return f'Mi habilidad es: {self.habilidad}'

class EmpleadoArtista(Persona, Artista):
    def __init__(self, nombre, edad, nacionalidad, habilidad, salario, empresa):
        Persona.__init__(self, nombre, edad, nacionalidad)
        Artista.__init__(self, habilidad)
        self.salario = salario
        self.empresa = empresa
        
    def presentarse(self):
        print(f'Hola, me llamo {self.nombre}, tengo {self.edad} años y {self.nacionalidad}. {self.mostrar_habilidades()}')

roberto = EmpleadoArtista("Roberto", 30, "Mexicano", "Pintura", 50000, "Google")

# print(roberto.salario)
# roberto.presentarse()
herencia = issubclass(EmpleadoArtista, Persona)
instancia = isinstance(roberto, Persona)
print(herencia)
print(instancia)
