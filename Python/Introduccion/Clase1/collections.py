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

# No se pueden mutar las tuplas. Hace que sea mas eficiente en memoria y mas rapida para acceder a sus elementos, pero no se pueden modificar después de su creación.
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
print(f"Diferencia simétrica: {diferencia_simetrica} \n")

conjunto_c = {3, 1, 2} # Ordena automáticamente los elementos, no mantiene el orden de inserción
print(f"Conjunto C: {conjunto_c} \n")

conjunto_c.add(4)  # Agregar un elemento al conjunto
print(f"Conjunto C después de agregar 4: {conjunto_c} \n")

conjunto_c.remove(2)  # Eliminar un elemento del conjunto
print(f"Conjunto C después de eliminar 2: {conjunto_c} \n")
      
conjunto_c.discard(100)  # Eliminar un elemento del conjunto sin generar error si no existe
print(f"Conjunto C después de intentar eliminar 100: {conjunto_c} \n")

conjunto_c.clear()  # Eliminar todos los elementos del conjunto
print(f"Conjunto C después de limpiar: {conjunto_c} \n")

# Zip
nombres = ["Alice", "Bob", "Charlie", "David", "Eve"]  # Lista más larga para mostrar que zip se detiene
edades = [25, 30, 35, 40]

combinados = zip(nombres, edades)
print(f"Combinados: {list(combinados)} \n")

# Rangos
rango1 = range(5)  # Crea un rango de 0 a 4. START, STOP, STEP

list(rango1)  # Convertir el rango a una lista para mostrar sus elementos
print(f"Rango1: {list(rango1)} \n")

# Tambien de esta otra forma
print(*range(100))

rango2 = range(10, 30)
print(f"Rango2: {list(rango2)} \n")

rango3 = range(0, 20, 2)
print(f"Rango3: {list(rango3)} \n")

rango4 = range(70, 50)
print(f"Rango4: {list(rango4)} \n")

rango5 = range(70, 50, -1)
print(f"Rango5: {list(rango5)} \n")