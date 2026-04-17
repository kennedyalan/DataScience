# Numpy
import numpy as np
# Práctica común: definir numpy as np

def salto_de_linea(texto):
    return "=" * 20 + texto + "=" * 20

# Arrays vs listas de Python
# Las listas pueden contener cualquier tipo de dato.
# Los arrays de numpy son homogéneos (todos del mismo tipo),
# lo que los hace más eficientes en memoria y velocidad.

# Creación de arrays a partir de una lista de Python
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
print(array_dimensiones.shape)  # Devuelve una tupla con (filas, columnas)


print(salto_de_linea(" Acceso a elementos "))

print(array_dimensiones[0])     # Primera fila
print(array_dimensiones[2])     # Última fila
print(array_dimensiones[2, 2])  # Tercera fila, tercera columna
print(array_dimensiones[2][2])  # Ídem, forma alternativa


print(np.zeros((3, 5)))
print(np.ones((3, 5)))

# arange: como range() pero devuelve un array de numpy
# np.arange(inicio, fin_excluido, paso) → [0, 2, 4, 6, 8]
print(np.arange(0, 10, 2))

# linspace: genera N puntos equidistantes entre inicio y fin (ambos incluidos)
# Útil para construir el eje x en gráficas
np.linspace(0, 100, 13)

array_ejemplo = np.array([[[3, 6, 9], [12, 15, 18]],
                          [[21, 24, 27], [30, 33, 36]],
                          [[39, 42, 45], [48, 51, 54]]])

print(salto_de_linea(" Ejercicio "))
# Ejercicio: números impares del 1 al 19
# ¿Qué diferencia hay entre arange() y linspace() aquí?
print(np.arange(1, 20, 2))
count = len([i for i in range(1, 20) if i % 2 != 0])
print(np.linspace(1, 19, count, dtype=int))  # No es tan directo, hay que calcular los numeros de sample que hay que generar.
                                  # Otra diferencia es que genera floats, no enteros.

print(salto_de_linea(" Ordenar, agregar y borrar elementos "))
print(np.sort([2, 1, 5, 3, 7, 4, 6, 8]))

array_ordenado = np.sort(array_ejemplo)
print(f"Array ordenado: \n{array_ordenado}")
print(f"Array en orden inverso: \n{array_ordenado[::-1]}")

print(salto_de_linea(" Metodos que vamos a necesitar siempre "))
print(array_ejemplo)
print(array_ejemplo.shape)
print(array_ejemplo.ndim)
print(array_ejemplo.size)

print(salto_de_linea(" Reshape "))
reshape = np.arange(10)
print(f"Original: {reshape}")

reshape = reshape.reshape(5, 2)
reshape2 = reshape.reshape(2, 5)
print(f"Reshape caso 1: \n{reshape}")
print(f"Reshape caso 2: \n{reshape2}")

print(f"Traspuesta caso 1: \n{reshape.T}")

print(salto_de_linea(" Logicas "))
ar = np.arange(5,20)
print(f"Array: \n{ar}")

print(ar[ar > 10]) # Esto devuelve una nueva lista, en el print no hace falta pero sirve para asignarlo a una variable.

mayores_que_10 = ar[ar > 10]
print(f"Mayores que 10: \n{mayores_que_10}")

print(f"Mayores que 5 y pares: \n{ar[(ar > 5) & (ar % 2 == 0)]}")

print(salto_de_linea(" Axis "))
array_axis = np.array([[1, 2, 3],
                       [1, 2, -2]])

print(f"Array original: \n{array_axis}")
print(f"Suma por columnas (axis=0): \n{array_axis.sum(axis=0)}")
print(f"Suma por filas (axis=1): \n {array_axis.sum(axis=1)})")