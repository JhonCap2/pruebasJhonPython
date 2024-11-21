# Poder quitar los espacios

def no_espacio(texto):
    nuevo_texto = ""
    for char in texto:
        if char != " ":
            nuevo_texto += char
    return nuevo_texto


# Poder dar vuelta a un texto
def reverse(texto):
    texto_al_reves = ""
    for char in texto:
        texto_al_reves = char + texto_al_reves
    return (texto_al_reves)

# Validar un texto con otro


def es_palindromo(texto):
    texto = no_espacio(texto)
    texto_al_reves = reverse(texto)
    return texto.lower() == texto_al_reves.lower()


print(es_palindromo("Amo la paloma"))
print(es_palindromo("HolaMundo"))
