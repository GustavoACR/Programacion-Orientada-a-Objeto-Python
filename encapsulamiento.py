class MiClase:
    def __init__(self):
        self._atributo_protegido = "Este es un atributo protegido"
        self.__atributo_privado = "Este es un atributo privado"
        
    def __hablar(self):
        return "Este es un método privado"
        
objeto = MiClase()
print(objeto._MiClase__atributo_privado)
print(objeto._MiClase__hablar())