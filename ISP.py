from abc import ABC, abstractclassmethod

# class Trabajador(ABC):
    
#     @abstractclassmethod
#     def comer(self):
#         pass
    
#     def trabajar(self):
#         pass
    
#     def dormir(self):
#         pass
    
# class Humano(Trabajador):
#     def comer(self):
#         print("El humano está comiendo")

#     def trabajar(self):
#         print("El humano está trabajando")

#     def dormir(self):
#         print("El humano está durmiendo")
        
# class Robot(Trabajador):
#     def comer(self):
#         pass

#     def trabajar(self):
#         print("El robot está trabajando")

#     def dormir(self):
#         pass
    
    
class Trabajador(ABC):
    
    @abstractclassmethod
    def trabajar(self):
        pass
    
class Comerdor(ABC):
    
    @abstractclassmethod
    def comer(self):
        pass
    
class Durmiente(ABC):
    
    @abstractclassmethod
    def dormir(self):
        pass

class Humano(Trabajador, Durmiente, Comerdor):
    def comer(self):
        print("El humano está comiendo")

    def trabajar(self):
        print("El humano está trabajando")

    def dormir(self):
        print("El humano está durmiendo")
        
class Robot(Trabajador):
    
    def trabajar(self):
        print("El robot está trabajando")
        
robot = Robot()
humano = Humano()

robot.trabajar()
humano.trabajar()
humano.comer()
humano.dormir()