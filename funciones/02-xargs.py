def suma(*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(resultado)


suma(2, 7, 10)
suma(2, 6)
suma(3, 4, 5, 6, 15)
