# Numpy
import numpy as np
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