# 1. Crear una lista:
mi_lista = [1, 2, 3, 'cuatro', True]

# 2. Acceder a elementos de la lista:
print(mi_lista[0]) # 1
print(mi_lista[-1]) # True


# 3. Cambiar elementos en la lista:
mi_lista[0] = 'uno'
print(mi_lista) # ['uno', 2, 3, 'cuatro', True]


# 4. Añadir elementos a la lista:
mi_lista.append('cinco')
print(mi_lista) # ['uno', 2, 3, 'cuatro', True, 'cinco']


# 5. Eliminar elementos de la lista:
del mi_lista[3]
print(mi_lista) # ['uno', 2, 3, True, 'cinco']


# 6. Unir dos listas:
otra_lista = [6, 7, 8]
mi_lista.extend(otra_lista)
print(mi_lista) # ['uno', 2, 3, True, 'cinco', 6, 7, 8]


# 7. Ordenar la lista:
"""
mi_lista.sort()
print(mi_lista) # [True, 2, 3, 6, 7, 8, 'cinco', 'uno']

"""


# 8. Obtener la longitud de la lista:
print(len(mi_lista)) # 8

