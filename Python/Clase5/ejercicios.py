import numpy as np

def salto_de_linea(texto):
    return "=" * 20 + texto + "=" * 20

print(salto_de_linea(" Ejercicio - Números impares "))
# Ejercicio: números impares del 1 al 19
# ¿Qué diferencia hay entre arange() y linspace() aquí?
print(np.arange(1, 20, 2))
count = len([i for i in range(1, 20) if i % 2 != 0])
print(np.linspace(1, 19, count, dtype=int))  # No es tan directo, hay que calcular los numeros de sample que hay que generar.
                                  # Otra diferencia es que genera floats, no enteros.

print(salto_de_linea(" Ejercicio - Matriz de temperaturas y filtrado con NumPy "))
# Generá una **matriz 30×30** de temperaturas aleatorias entre **0 °C y 50 °C** usando NumPy.
# Luego, filtrá las temperaturas:
# - menores a **5 °C**
# - o mayores a **35 °C**
temperaturas = np.random.uniform(0, 50, (30, 30))
print(f"Matriz de temperaturas: \n{np.round(temperaturas, 2)}")

temperaturas_filtradas = np.round(temperaturas[(temperaturas < 5) | (temperaturas > 35)], 2).astype(int)
print(f"Temperaturas filtradas (menores a 5 °C o mayores a 35 °C): \n{temperaturas_filtradas}")


print(salto_de_linea(" Ejercicio - 1.60 "))
# Crea un arreglo a partir de la lista [1, 2, 3, 4, 5]. Suma 10 a cada elemento y multiplica el resultado por 2.

arreglo = np.array([1, 2, 3, 4, 5])

resultado = (arreglo + 10) * 2
print(f"Resultado: \n{resultado}")

print(salto_de_linea(" Ejercicio - 1.61 "))
# Genera un arreglo de 3x3 con números del 1 al 9. Calcula la suma de cada fila y de cada columna.
matriz_3 = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])

suma_columnas = np.sum(matriz_3, axis=0)
suma_filas = np.sum(matriz_3, axis=1)
print(f"Suma de columnas: \n{suma_columnas}")
print(f"Suma de filas: \n{suma_filas}")

print(salto_de_linea(" Ejercicio - 1.62 "))
# Crea un arreglo de 100 números aleatorios entre 0 y 1. Calcula la media y la desviación estándar.
arreglo100 = np.random.random(100)
print(f"Arreglo de 100 números aleatorios entre 0 y 1: \n{arreglo100}")
media = np.mean(arreglo100)
print(f"Media del arreglo: {media}")
desvio_estandar = np.std(arreglo100)
print(f"Desvío estándar del arreglo: {desvio_estandar}")

print(salto_de_linea(" Ejercicio - 1.63 "))
# Dado un arreglo de 4x4, extrae los elementos de la segunda fila y la tercera columna.
matriz_4 = np.random.randint(0, 10, (4, 4))
print(f"Matriz de 4x4: \n{matriz_4}")
segunda_fila = matriz_4[1, :]
tercera_columna = matriz_4[:, 2]

print(f"Elementos de la segunda fila: \n{segunda_fila}")
print(f"Elementos de la tercera columna: \n{tercera_columna}")

print(salto_de_linea(" Ejercicio - 1.64 "))
# Resuelve el sistema de ecuaciones:
# 2x + y = 5
# x - y = 1

coeficientes = np.array([[2, 1], [1, -1]])
independientes = np.array([5, 1])

solucion = np.linalg.solve(coeficientes, independientes).astype(int)
print(f"Solución del sistema de ecuaciones: \n{solucion}")

print(salto_de_linea(" Ejercicio - 1.65 "))
# Crea una matriz de 5x5 con valores del 0 al 24 e intercambia la primera fila con la última fila de forma eficiente.
matriz_5 = np.random.randint(0, 25, (5 , 5))
print(f"Matriz de 5x5: \n{matriz_5}")
matriz_5[[0, -1]] = matriz_5[[-1, 0]]
print(f"Matriz después de intercambiar la primera y última fila: \n{matriz_5}")

print(salto_de_linea(" Ejercicio - 1.66 "))
# Genera un arreglo de 20 números enteros aleatorios (1-100) y sustituye todos los múltiplos de 3 por el valor 999.
arreglo20 = np.random.randint(0, 100, 20)
arreglo20.sort()
print(f"Arreglo de 20 números aleatorios entre 0 y 100: {arreglo20}")

arreglo20[arreglo20 % 3 == 0] = 999
print(f"Arreglo de 20 números aleatorios entre 0 y 100: {arreglo20}")

print(salto_de_linea(" Ejercicio - 1.67 "))
# Utiliza broadcasting para crear una matriz de 4x4 donde cada fila sea la secuencia [10, 20, 30, 40].
secuencia = np.array([10, 20, 30, 40])
ones = np.ones((4, 1))
matriz_broadcast = (ones * secuencia).astype(int)
print(f"Matriz de 4x4 con broadcasting: \n{matriz_broadcast}")

print(salto_de_linea(" Ejercicio - 1.68 "))
# Crea un arreglo de 5x5 con números aleatorios y encuentra los índices (fila, columna) de su valor máximo.

matriz_5x5 = np.random.randint(0, 100, (5, 5))
print(f"Matriz de 5x5: \n{matriz_5x5}")
maximo = np.max(matriz_5x5)
indices_maximo = np.where(matriz_5x5 == maximo)
print(f"Valor máximo: {maximo}")
print(f"Índices del valor máximo (fila, columna): \n{indices_maximo}")

print(salto_de_linea(" Ejercicio - 1.69 "))
# Genera 15 números aleatorios y cuenta cuántos de ellos son superiores al promedio del arreglo.
arreglo_15 = np.random.randint(0, 100, 15)
mean = np.mean(arreglo_15).astype(int)
cont = np.sum(arreglo_15 > mean)
print(f"Arreglo de 15 números aleatorios entre 0 y 100: \n{arreglo_15}")
print(f"Media del arreglo: {mean}")
print(f"Números mayores que la media: {cont}")

print(salto_de_linea(" Ejercicio - 1.70 "))
# Crea una matriz de 8x8 que represente un tablero de ajedrez (0 y 1 alternados) usando slicing con pasos.
ajedrez = np.zeros((8 ,8))
ajedrez[0::2, 1::2] = 1
ajedrez[1::2, 0::2] = 1
print(f"Matriz de ajedrez 8x8: \n{ajedrez.astype(int)}")

print(salto_de_linea(" Ejercicio - 1.71 "))
# Crea dos arreglos de 10 números aleatorios y encuentra los valores que están presentes en ambos (intersección).
arreglo_01 = np.random.randint(0, 10, 10)
arreglo_02 = np.random.randint(0, 10, 10)
interseccion = np.intersect1d(arreglo_01, arreglo_02)
print(f"Arreglo 1: \n{arreglo_01}")
print(f"Arreglo 2: \n{arreglo_02}")
print(f"Intersección de ambos arreglos: \n{interseccion}")