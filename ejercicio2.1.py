class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        print(f"Hola, me llamo {self.nombre} y tengo {self.edad} años.")

class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado
        
    def mostrar_grado(self):
        print(f"Estoy en {self.grado} grado.")
        
Jose = Estudiante("Jose", 20, "decimo")
print(f"""
      DATOS DEL ESTUDIANTE:\n
      Nombre: {Jose.nombre}\n
      Edad: {Jose.edad}\n
      Grado: {Jose.grado}\n
      """)
Jose.presentarse()
Jose.mostrar_grado()
