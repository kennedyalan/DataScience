"""
Comentarios en Python
"""

# Comentarios de una sola línea

print("Hola, mundo!")

# Variables
variable1 = 14
variable2 = 3.14
variable3 = 34+4j

booleano1 = False
booleano2 = True

string1 = "Hola"
string2 = 'Mundo'

variables = [variable1, variable2, variable3, booleano1, booleano2, string1, string2]
for variable in variables:
    print(f"La variable es: {variable}")
    print(f"Es de tipo: {type(variable)}\n")


# Leer datos
dato = input("Ingrese su nombre: ")
print(f"El nombre ingresado es: {dato}")

# Conversiones
numero1 = input("Ingrese un número entero: ")
numero1 = int(numero1)  # Convertir a entero
print(f"El número ingresado es: {numero1} y es de tipo: {type(numero1)}")