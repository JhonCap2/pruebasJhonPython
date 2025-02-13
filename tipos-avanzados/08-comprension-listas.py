usuarios = [
    ["Jhon", 3],
    ["Leonard", 5],
    ["Lisbeth", 1]
]

# nombres = []
# for usuario in usuarios:
#    nombres.append(usuario[0])
# print(nombres)

# imprimir nombres- map
# El 0 es para llamar el primer elemento que sera el nombre
# nombres = [usuario[0] for usuario in usuarios]

# filtrar- Filter
# nombres = [usuario for usuario in usuarios if usuario[1] > 2]

# Filtrada y transformada- map and filter
# nombres = [usuario[0] for usuario in usuarios if usuario[1] > 2]


# nombres = list(map(lambda usuario: usuario[0], usuarios))
# Estos son a preferencia del programador
menosUsuarios = list(filter(lambda usuario: usuario[1] > 2, usuarios))
print(menosUsuarios)
