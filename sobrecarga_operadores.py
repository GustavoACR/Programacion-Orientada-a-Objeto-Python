class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def __str__(self):
        return f"Persona(nombre={self.nombre},edad={self.edad})"
    
    def __repr__(self):
        return f"Persona('{self.nombre}', {self.edad})"
    
    def __add__(self, other):
        nuevo_valor = self.edad + other.edad
        return Persona(self.nombre + " " + other.nombre, nuevo_valor)
    
gus = Persona("Gustavo", 30)
pedro = Persona("Pedro", 25)
print(gus + pedro)
