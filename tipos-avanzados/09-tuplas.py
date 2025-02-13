# Cuando no queramos modificar elementos de una lista
numeros = (1, 2, 3) + (4, 5, 6)
print(numeros)

punto = tuple([1, 2])
print(punto)

menosNumero = numeros[:2]
print(menosNumero)

primero, segundo, *otros = numeros
print(primero, segundo, otros)

for n in numeros:
    print(n)
