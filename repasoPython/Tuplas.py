# 1. Crear una tupla vacía:
tupla_vacia = ()
print(tupla_vacia)

# 2. Crear una tupla con un solo elemento:
tupla_uno = (1,)
print(tupla_uno)
# 3. Crear una tupla con varios elementos:
tupla_varios = (1, 2, 3, 4)
print(tupla_varios)

# 4. Convertir una lista en una tupla:
lista = [1, 2, 3, 4]
tupla = tuple(lista)
print(tupla)
# 5. Acceder a los elementos de una tupla:
tupla = (1, 2, 3, 4)
print(tupla[0]) # resultado: 1


# 6. Obtener la longitud de una tupla:
tupla = (1, 2, 3, 4)
print(len(tupla)) # resultado: 4


# 7. Concatenar tuplas
tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)
tupla_concatenada = tupla1 + tupla2
print(tupla_concatenada)

# 8. Desempaquetar una tupla:
tupla = (1, 2, 3, 4)
a, b, c, d = tupla
print(a,b,c,d)

# ejercicios con tuplas
# 1.
fruits = ("apple", "banana", "cherry")
print(fruits[0])
# 2.
fruits = ("apple", "banana", "cherry")
print(fruits[-1])
# 3.
fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[2:5])

# tuplas anidadas
tupla_exterior = (1, 2, (3, 4), 5)
print(tupla_exterior)   # salida: (1, 2, (3, 4), 5)

# Acceder al elemento de la tupla exterior
print(tupla_exterior[2])   # salida: (3, 4)

# Acceder al elemento de la tupla interior
print(tupla_exterior[2][0])   # salida: 3

#
tupla = (1, 2, 3, 4)
tupla = (1, 2, 3, 4)
print(tupla[0])   # salida: 1
print(tupla[1])   # salida: 2
print(tupla[2])   # salida: 3
print(tupla[3])   # salida: 4

tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)
tupla3 = tupla1 + tupla2
print(tupla3)   # salida: (1, 2, 3, 4, 5, 6)

tupla = (1, 2, 3)
tupla_repetida = tupla * 3
print(tupla_repetida)   # salida: (1, 2, 3, 1, 2, 3, 1, 2, 3)

tupla = (1, 2, 3, 4)
longitud = len(tupla)
print(longitud)   # salida: 4

tupla = (1, 2, 3)
lista = list(tupla)
print(lista)   # salida: [1, 2, 3]
