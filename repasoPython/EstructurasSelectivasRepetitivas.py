# Selectivas
# If-else: esta estructura se utiliza para ejecutar diferentes bloques de código según una condición.
# Si la condición es verdadera, se ejecuta un bloque de código; de lo contrario, se ejecuta otro
# bloque de código.

x = 5

if x < 10:
    print("x es menor que 10")
else:
    print("x es mayor o igual a 10")

# If-elif-else: esta estructura se utiliza cuando hay varias condiciones que deben evaluarse.
# Si se cumple la primera condición, se ejecuta un bloque de código; de lo contrario, se evalúa la siguiente condición,
# y así sucesivamente. Si ninguna de las condiciones se cumple, se ejecuta un bloque de código por defecto.

x = 5

if x < 0:
    print("x es negativo")
elif x == 0:
    print("x es cero")
else:
    print("x es positivo")

# Repetitivas
# For: esta estructura se utiliza para repetir un bloque de código un número determinado de veces.
# Se puede iterar sobre una secuencia, como una lista o una cadena de texto.
for i in range(5):
    print(i)
# While: esta estructura se utiliza para repetir un bloque de código mientras se cumpla una condición.
# La condición se evalúa antes de cada repetición.
x = 5

while x > 0:
    print(x)
    x -= 1