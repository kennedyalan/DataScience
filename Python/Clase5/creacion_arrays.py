import numpy as np

def salto_de_linea(texto):
    return "=" * 20 + texto + "=" * 20

# Arrays vs listas de Python
# Las listas pueden contener cualquier tipo de dato.
# Los arrays de numpy son homogéneos (todos del mismo tipo),
# lo que los hace más eficientes en memoria y velocidad.

print(salto_de_linea(" Creación de arrays "))

lista = [1, 2, 3, 4, 5]
array = np.array(lista)
print(array)

array2 = np.array([5, 4, 3, 2, 1])
print(array2)

# Array de más dimensiones
# Tip: los colores distintos en VS Code indican el número de dimensiones
array_dimensiones = np.array([[1, 2, 3],
                              [4, 5, 6],
                              [7, 8, 9]])
print(array_dimensiones)
print(array_dimensiones.shape)

print(np.zeros((3, 5)))
print(np.ones((3, 5)))

# arange: como range() pero devuelve un array de numpy
# np.arange(inicio, fin_excluido, paso) → [0, 2, 4, 6, 8]
print(np.arange(0, 10, 2))

# linspace: genera N puntos equidistantes entre inicio y fin (ambos incluidos)
# Útil para construir el eje x en gráficas
np.linspace(0, 100, 13)
