# set significa grupo o conjunto, esta no se repite, ni se ordena.

primer = {1, 1, 2, 2, 3, 4}
# primer.add(5)
# primer.remove(1)

segundo = [3, 4, 5]
segundo = set(segundo)
# print(primer | segundo) esto va a juntar los set en 1

# print(primer & segundo) Este hace un solo si existen en el primero y tambien en el segundo los mostrara

# print(primer - segundo) Calcula la diferencia al primer set buscando la diferencia

# con Alt + 94 = ^
# print(primer ^ segundo) elimina los elementos duplicados en los dos set.


if 5 in segundo:
    print("hola mundo")
