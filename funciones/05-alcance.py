saludo = "Hola Global"  # no usar variables globales


def saludar():
    global saludo
    saludo = "Hola Mundo"


def saludaChanchito():
    saludo = "Hola Chanchito"
    print(saludo)


print(saludo)
saludar()
print(saludo)
