# Numpy
import Python.Clase5.librerias as np
## Practica comun definir numpy as np

# Arrays vs listas de python
# Las listas de python pueden contener cualquier tipo de dato, mientras que los arrays de numpy son homogéneos, es decir, 
# todos los elementos deben ser del mismo tipo de dato. 
# Esto hace que los arrays de numpy sean más eficientes en términos de memoria y velocidad de procesamiento.

# Creacion de arrays
# A partir de una lista de python
lista = [1, 2, 3, 4, 5]
array = np.array(lista)
print(array)

array2 = np.array([[1, 2, 3, 4, 5]])
print(array2)

# Mas dimensiones:
array_dimensiones = np.array([[1, 2, 3],
                              [4, 5, 6],
                              [7, 8, 9]]) # Tip: cuantos colores distintos se ven en vs code. Es el numero de dimensiones que tiene este array. En este caso, 3 dimensiones (profundidad, filas y columnas)
print(array_dimensiones)

## Acceso a elementos
print(array_dimensiones[0]) # Accede a la primera fila
print(array_dimensiones[2]) # Accede a la ultima fila
print(array_dimensiones[2, 3]) # Tercer fila, cuarta columna
print(array_dimensiones[2][3]) # tercer fila, cuarta columna (otra forma de acceder)


## Forma del array
array_dimensiones.shape # Devuelve una *tupla* con el numero de filas y columnas del array


## Eje x
np.linspace(0, 100, 13)
# Sirve para construir un eje x ya que esto genera 13 puntos equidistantes entre 0 y 100, incluyendo ambos extremos.

array_ejemplo = np.array([[[3, 6, 9], [12, 15, 18]], [[21, 24, 27], [30, 33, 36]], [[39, 42, 45], [48, 51, 54]]])

print(array_ejemplo.shape) # Devuelve (3, 2, 3) lo que significa que el array tiene 3 bloques, cada bloque tiene 2 filas y cada fila tiene 3 columnas.
print(array_ejemplo.ndim)
print(array_ejemplo.size) # Devuelve el numero total de elementos en el array, que es 18 (3 bloques x 2 filas x 3 columnas = 18 elementos)