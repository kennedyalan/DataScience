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
lista.append("Me inserté al final!")
print(f"{lista}\n")

# Insert - Agregar en una posición específica
lista.insert(2, "Me inserté en el index 2!")
print(f"{lista}\n")

# Eliminar de un índice específico
eliminar = [1, 3, 5, 7, 9]
print(f"Voy a eliminar el 7 de {eliminar}\n")
eliminar.pop(3)
print(f"Después de eliminar: {eliminar}\n")

# No se pueden mutar las tuplas
try:
    tupla[0] = 10  # Esto generará un error
except TypeError as e:
    print(f"Error: {e} \n")


# Diccionarios - Clave valor (como JSON)
d_frame = {
    "A": [1, 2, 3],
    "B": [3, 6, 9]
}
# Acceder a el valor 1 en la clave B
print(f"Diccionario: {d_frame}")
print(f"Valor de clave B: {d_frame['B']}")
print(f"Valor en clave B index 1: {d_frame['B'][1]}\n")

# Conjuntos - No permiten elementos duplicados
conjunto = {1, 2, 3, 4, 5, 5, 5}
print(f"Conjunto: {conjunto} \n")

# Operaciones
conjunto_a = {1, 2, 3, 4}
conjunto_b = {3, 4, 5, 6}

# Unión - todos los elementos en total sin repetidos
union = conjunto_a | conjunto_b
print(f"Unión: {union} \n")

# Intersección - elementos repetidos en ambos
interseccion = conjunto_a & conjunto_b
print(f"Intersección: {interseccion} \n")

# Diferencia - elementos en a que no están en b
diferencia = conjunto_a - conjunto_b
print(f"Diferencia: {diferencia} \n")

# Diferencia simétrica - elementos en a o b pero no en ambos. 
# Parecido a union pero esta diferencia elimina totalmente el repetido, la union mantiene al elemento que se repite pero solo una vez.
diferencia_simetrica = conjunto_a ^ conjunto_b