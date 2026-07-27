class Estudiante:
    def __init__ (self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado
        
    def estudiar(self):
        print(f"{self.nombre} está estudiando.")
        
nombre = input("Introduce el nombre del estudiante: ")
edad = int(input("Introduce la edad del estudiante: "))
grado = int(input("Introduce el grado del estudiante: "))

estudiante = Estudiante(nombre, edad, grado)

print(f"""
      DATOS DEL ESTUDIANTE: \n\n
      Nombre: {estudiante.nombre} \n
      Edad: {estudiante.edad} \n
      Grado: {estudiante.grado} \n
      
      """)

while True:
    estudiar = input()
    if (estudiar.lower() == "estudiar"):
       estudiante.estudiar()
       break
