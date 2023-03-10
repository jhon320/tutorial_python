
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

# lista enlazada
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None


class ListaEnlazada:
    def __init__(self):
        self.inicio = None

    def agregar_elemento(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.inicio is None:
            self.inicio = nuevo_nodo
        else:
            actual = self.inicio
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def imprimir_lista(self):
        actual = self.inicio
        while actual is not None:
            print(actual.valor)
            actual = actual.siguiente


lista = ListaEnlazada()
lista.agregar_elemento(1)
lista.agregar_elemento(2)
lista.agregar_elemento(3)
lista.imprimir_lista() # Imprime: 1 2 3


# operaciones con listas
lista1 = [1, 2, 3, 4, 5]
lista1.append(6)
print(lista1)

lista2 = ["manzana", "naranja", "pera"]
lista2.remove("naranja")
print(lista2)

lista3 = [4, 2, 6, 1, 3, 5]
lista3.sort()
print(lista3)

lista4 = [4, 2, 6, 1, 3, 5]
busqueda = lista4.index(3)
print(busqueda)
