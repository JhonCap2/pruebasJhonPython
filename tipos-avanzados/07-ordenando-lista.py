numeros = [2, 4, 8, 11, 27, 35, 55, 75, 100, 9, 30]

# numeros.sort(reverse=True)

numeros2 = sorted(numeros, reverse=True)
print(numeros)
print(numeros2)

# usuarios = [[2, "Jhon"], [3, "Leonard"], [1, "Lisbeth"]]
usuarios = [["Jhon", 3], ["Leonard", 5], ["Lisbeth", 1]]


# def ordena(elemento):
#    return elemento[1]


usuarios.sort(key=lambda el: el[1], reverse=True)
print(usuarios)
