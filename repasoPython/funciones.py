# Entradas
base = float(input("Ingrese base: "))
altura = float(input("Ingrese altura"))

# Proceso
def calcularAriaTriangulo(b,al):
    area = (b*al)/2
    area = (b * al) / 2
    return area

# Salida
resultado = calcularAriaTriangulo(base, altura)
print("El area del trinangulo es:", resultado)

# Funciones con argumentos por defeto
def mostrarPais(pais="Colombia"):
    print("Yo soy de: " + pais)

mostrarPais("Canada")
mostrarPais("Ecuador")
mostrarPais()
mostrarPais("Brazil")