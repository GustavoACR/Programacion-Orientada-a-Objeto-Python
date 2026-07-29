class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_edad(self):
        return self._edad

    def set_edad(self, edad):
        self._edad = edad
        
gus = Persona("Gustavo", 25)
print(gus.get_nombre())
print(gus.get_edad())
gus.set_nombre("Gustavo Adolfo")
gus.set_edad(26)
print(gus.get_nombre())
print(gus.get_edad())