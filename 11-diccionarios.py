# colecion de datos por llave y identificador


punto = {"x": 25, "y": 50}
print(punto)
print(punto["x"])
print(punto["y"])

punto["z"] = 45
print(punto)


if "lala" in punto:
    print("Encontre lala", punto["lala"])


print(punto.get("x"))

del punto["x"]
del (punto["y"])

print(punto)

punto["x"] = 25


for valor in punto:
    print(valor, punto[valor])


for valor in punto.items():
    print(valor)

for llave, valor in punto.items():
    print(llave, valor)


usuarios = [
    {"id": 1, "nombre": "Jhon"},
    {"id": 2, "nombre": "Leonard"},
    {"id": 3, "nombre": "Fabio"},
    {"id": 4, "nombre": "El Chibu"}
]

for usuario in usuarios:
    print(usuario["nombre"])
