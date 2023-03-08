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
