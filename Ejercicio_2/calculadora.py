numero = int(input("Ingresa un número decimal: "))

def convertir(numero, base):
    if numero == 0:
        return "0"
    
    digitos = "0123456789ABCDEF"
    resultado = ""
    
    while numero > 0:
        residuo = numero % base
        resultado = digitos[residuo] + resultado
        numero = numero // base
    
    return resultado


print("\nResultados:")
print("Binario:", convertir(numero, 2))
print("Octal:", convertir(numero, 8))
print("Hexadecimal:", convertir(numero, 16))


