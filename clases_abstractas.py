from abc import ABC, abstractclassmethod

class Persona(ABC):
    @abstractclassmethod
    def __init__(self, nombre, edad, sexo, actividad):
        self._nombre = nombre
        self._edad = edad
        self._sexo = sexo
        self._actividad = actividad
        
    @abstractclassmethod
    def hacer_actividad(self):
        pass
    
    def presentarse(self):
        print(f"Me llamo {self._nombre}, tengo {self._edad} años, soy {self._sexo} y me dedico a {self._actividad}")
        
#gus = Persona("Gustavo", 30, "masculino", "ingeniería")

class Estudiante(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)

    def hacer_actividad(self):
        print(f"Estoy estudiando {self._actividad}")
        
class Trabajador(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)

    def hacer_actividad(self):
        print(f"Estoy trabajando en {self._actividad}")
        
gus = Estudiante("Gustavo", 30, "masculino", "programacion")
jose = Trabajador("José", 35, "masculino", "contabilidad")

gus.presentarse()
jose.presentarse()
gus.hacer_actividad()
jose.hacer_actividad()
