# Operaciones matematicas

# numero = input("Ingrese un numero: ")
numero = 54
numero = float(numero)  # Convertir a flotante

print(numero + 10)  # Suma
print(numero - 5)   # Resta

print(numero * 2)   # Multiplicacion
print(numero / 3)   # Division

print(numero // 2)  # Division entera
print(numero % 2)   # Modulo
print(numero ** 2)  # Potencia

print(54^2)  # XOR (operador bit a bit)

import math
print(dir(math))  # Mostrar funciones disponibles en el módulo math
print("\n")


# Colecciones

lista = [1, 2, 3, "hola", True]
tupla = (1, 2, 3, 4, 5)
diccionario = {
    "a": 1,
    "b": 2,
    "c": 3
}
colecciones = [lista, tupla, diccionario]
for coleccion in colecciones:
    print(f"La colección es: {coleccion}")
    print(f"La longitud es: {len(coleccion)}")
    print(f"Es de tipo: {type(coleccion)}\n")


# Append - Agregar a lo ultimo de la lista
print(lista.append("nuevo elemento"))

# Insert - Agregar en una posición específica
print(lista.insert(2, "Me inserté en el 2!"))