def mi_decorador(funcion):
    def funcion_modificada():
        print("Antes de llamar a la función")
        funcion()
        print("Después de llamar a la función")
    return funcion_modificada

# def saludo():
#     print("Hola, mundo!")

# saludo_decorada = mi_decorador(saludo)
# saludo_decorada()

@mi_decorador
def saludo():
    print("Hola, mundo!")

saludo()