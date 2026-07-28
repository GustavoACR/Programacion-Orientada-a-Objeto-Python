class A:
    def hablar(self):
        print("Hola, soy A")

class B(A):
    def hablar(self):
        print("Hola, soy B")

class C(A):
    def hablar(self):
        print("Hola, soy C")

class D(B, C):
    def hablar(self):
        print("Hola, soy D")
        
d = D()
d.hablar()
print(D.mro())
