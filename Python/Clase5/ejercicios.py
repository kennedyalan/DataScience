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
print(f"Matriz de temperaturas: \n{temperaturas}")

temperaturas_filtradas = np.round(temperaturas[(temperaturas < 5) | (temperaturas > 35)]).astype(int)
print(f"Temperaturas filtradas (menores a 5 °C o mayores a 35 °C): \n{temperaturas_filtradas}")
