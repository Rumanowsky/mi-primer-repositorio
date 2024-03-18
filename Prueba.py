vocales = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
numero_vocales = 0
numero_espacios = 0
frase = str(input("Introduce una frase: "))

for cada_caracter in frase:
    if cada_caracter in vocales:
        numero_vocales += 1
    elif cada_caracter == " ":
        numero_espacios += 1

print("El numero de vocales es: ", numero_vocales)
print("El numero de espacios es: ", numero_espacios)