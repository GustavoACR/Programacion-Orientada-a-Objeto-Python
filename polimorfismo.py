class Animal():
    def sonido(self):
        pass

class Gato(Animal):
    def sonido(self):
        return "Miau"

class Perro(Animal):
    def sonido(self):
        return "Guau"
    
def hacer_sonido(animal):
    return animal.sonido()

gato = Gato()
perro = Perro()

print(hacer_sonido(gato))
print(hacer_sonido(perro))

#duck typing
#En Python, el duck typing se basa en la idea de que si un objeto se comporta como un pato, entonces se trata como un pato.
#Enlaces dinámicos
#En Python, los enlaces dinámicos significan que la decisión sobre qué método llamar se toma en tiempo de ejecución, no en tiempo de compilación.
#Enlazado estático
#Enlazado estático significa que la decisión sobre qué método llamar se toma en tiempo de compilación, no en tiempo de ejecución.
#tipo real
#En Python, el tipo real de un objeto se determina en tiempo de ejecución.
#tipo declarado
#En Python, el tipo declarado de un objeto se determina en tiempo de compilación.
