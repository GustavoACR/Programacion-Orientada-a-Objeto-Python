# class Diccionario:
#     def verificar_palabras(self, palabra):
#         # Lógica para verificar si la palabra existe en el diccionario
#         pass
    
# class CorrectorOrtografico:
#     def __init__(self):
#         self.diccionario = Diccionario()

#     def corregir_texto(self, texto):
#         # Lógica para corregir el texto utilizando el diccionario
#         pass

from abc import ABC, abstractclassmethod

class VerificadorOrtografico(ABC):
    @abstractclassmethod
    def verificar_palabras(self, palabra):
        pass
    
class Diccionario(VerificadorOrtografico):
    def verificar_palabras(self, palabra):
        # Lógica para verificar si la palabra existe en el diccionario
        pass
    
class CorrectorOrtografico:
    def __init__(self, verificador: VerificadorOrtografico):
        self.verificador = verificador

    def corregir_texto(self, texto):
        # Lógica para corregir el texto utilizando el diccionario
        pass