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
print(lista.insert(2, "Me inserté en el index 2!"))

# Eliminar de un índice específico
eliminar = [1, 3, 5, 7, 9]
print(eliminar.pop(3))

# No se pueden mutar las tuplas
try:
    tupla[0] = 10  # Esto generará un error
except TypeError as e:
    print(f"Error: {e}")


# Diccionarios - Clave valor (como JSON)
d_frame = {
    "A": [1, 2, 3],
    "B": [3, 6, 9]
}
# Acceder a el valor 1 en la clave B
print(d_frame["B"][1])

# Conjuntos - No permiten elementos duplicados
conjunto = {1, 2, 3, 4, 5, 5, 5}
print(conjunto)