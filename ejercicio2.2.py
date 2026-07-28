class Animal:
    def comer(self):
        print("Animal comiendo...")
        
class Mamifero(Animal):
    def amamantar(self):
        print("Animal amamantando...")
        
class Ave(Animal):
    def volar(self):
        print("Animal volando...")
        
class Murcielago(Mamifero, Ave):
    pass
    # def comer(self):
    #     print("Murcielago comiendo...")

    # def amamantar(self):
    #     print("Murcielago amamantando...")

    # def volar(self):
    #     print("Murcielago volando...")
        
murcielago = Murcielago()
murcielago.comer()
murcielago.amamantar()
murcielago.volar()