class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre
        
    @nombre.deleter
    def nombre(self):
        del self.__nombre

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, edad):
        self.__edad = edad
        
gus = Persona("Gustavo", 25)

print(gus.nombre)
print(gus.edad)

gus.nombre = "Gustavo Adolfo"
gus.edad = 26

#del gus.nombre

print(gus.nombre)
print(gus.edad)