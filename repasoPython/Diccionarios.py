# Para crear un diccionario en Python, se utiliza la sintaxis de llaves ({}) y se separan los pares clave-valor
# con dos puntos (:), y se separan los elementos del diccionario con comas.

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(
car.get("model")
)

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["year"] = 2020


diccionario1 = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}
diccionario1["profesion"] = "programador"
print(diccionario1)

diccionario2 = {"nombre": "Maria", "edad": 25, "ciudad": "Barcelona"}
del diccionario2["edad"]
print(diccionario2)

diccionario3 = {"nombre": "Pedro", "edad": 35, "ciudad": "Valencia"}
busqueda = diccionario3.get("edad")
print(busqueda)
