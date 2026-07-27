# celular1_marca = "samsung"
# celular2_marca = "appel"
# celular3_marca = "huawei"

# celular1_modelo = "S23"
# celular2_modelo = "iPhone 15 pro"
# celular3_modelo = "P20 pro"

# celular1_camaraT = "48MP"
# celular1_camaraT = "48MP"
# celular1_camaraT = "12MP"

# celular1_camaraF = "24MP"
# celular1_camaraF = "24MP"
# celular1_camaraF = "8MP"

#definiendo una clase con parámetros estaticos para crear objetos
# class Celular():
#     marca = "samsung"
#     modelo = "S23"
#     camaraT = "48MP"
#     camaraF = "24MP"
    
# celular1 = Celular()
# print(celular1.marca)
# print(celular1.modelo)
# print(celular1.camaraT)
# print(celular1.camaraF)

#definiendo una clase con parámetros dinámicos para crear objetos
class Celular:
    # Método constructor
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara
        
    def llamar(self):
        print(f"Estas en una llamada desde un: {self.marca}")
        
    def cortar(self):
        print(f"Has cortado la llamada desde un: {self.marca}")

celular1 = Celular("samsung", "S23", "48MP")
celular2 = Celular("appel", "iPhone 15 pro", "12MP")

# print(celular2.marca)
# print(celular2.modelo)
# print(celular2.camara)

# print(celular1.marca)
# print(celular1.modelo)
# print(celular1.camara)

#usando los métodos
celular1.llamar()
celular1.cortar()



