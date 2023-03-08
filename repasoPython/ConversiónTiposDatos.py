# Conversión de cadenas a enteros:
# Para convertir una cadena a un entero, podemos utilizar la función int().

cadena1 = "123"
entero1 = int(cadena1)
print(entero1)

# Conversión de enteros a cadenas:
# Para convertir un entero a una cadena, podemos utilizar la función str().
entero2 = 123
cadena2 = str(entero2)
print(cadena2)

# Conversión de cadenas a flotantes:
# Para convertir una cadena a un flotante, podemos utilizar la función float().

cadena3 = "3.14"
flotante1 = float(cadena3)
print(flotante1)

# Conversión de flotantes a enteros:
# Para convertir un flotante a un entero, podemos utilizar la función int(). Esto truncará cualquier fracción del número.

flotante2 = 3.14
entero3 = int(flotante2)
print(entero3)
# Conversión de enteros a flotantes:
# Para convertir un entero a un flotante, simplemente podemos asignar el valor a una variable flotante.
entero4 = 123
flotante3 = float(entero4)
print(flotante3)
# Conversión de cadenas a listas:
# Para convertir una cadena a una lista, podemos utilizar el método split().
cadena4 = "1,2,3,4,5"
lista1= cadena4.split(",")
print(lista1)
# Conversión de listas a cadenas:
# Para convertir una lista a una cadena, podemos utilizar el método join().
lista2 = ["1", "2", "3", "4", "5"]
cadena5 = ",".join(lista2)
print(cadena5)
