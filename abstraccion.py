class Auto():
    def __init__(self):
        self.estado = "apagado"
        
    def encender(self):
        self.estado = "encendido"
        print("Auto encendido")

    def conducir(self):
        if self.estado == "apagado":
            self.encender()
            print("Auto en marcha")
            
mi_auto = Auto()
mi_auto.conducir()