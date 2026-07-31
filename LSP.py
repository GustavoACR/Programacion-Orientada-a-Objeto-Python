# class Pajaro:
#     def volar(self):
#         print("Estoy volando")

# class Pinguino(Pajaro):
#     def volar(self):
#         print("No puedo volar, soy un pingüino")
        
# def hacer_volar(pajaro: Pajaro):
#     pajaro.volar()

# hacer_volar(Pinguino())

class Ave:
    pass

class AveVoladora(Ave):
    def volar(self):
        print("Estoy volando")
        
class AveNoVoladora(Ave):
    def volar(self):
        print("No puedo volar, soy un ave no voladora")