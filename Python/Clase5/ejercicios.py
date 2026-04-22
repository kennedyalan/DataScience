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

arreglo100 = np.random.random(100)
print(f"Arreglo de 100 números aleatorios entre 0 y 1: \n{arreglo100}")
media = np.mean(arreglo100)
print(f"Media del arreglo: {media}")
desvio_estandar = np.std(arreglo100)
print(f"Desvío estándar del arreglo: {desvio_estandar}")