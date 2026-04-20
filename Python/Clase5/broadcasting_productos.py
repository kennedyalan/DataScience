import numpy as np

def salto_de_linea(texto):
    return "=" * 20 + texto + "=" * 20

print(salto_de_linea(" Broadcasting "))
# Broadcasting: permite realizar operaciones entre arrays de diferentes formas y tamaños.
# Adapta automaticamente las dimensiones para que puedan operar.
data = np.array([1.5, 2.3, 3.7])
print(f"Data original: \n{data}")
print(f"Data * 1.6: \n{data * 1.6}")

print(salto_de_linea(" Producto punto "))
punto1 = np.array([1, 2, 3])
punto2 = np.array([3, 2, 1])

print(punto1.dot(punto2))  # Producto punto: 1*3 + 2*2 + 3*1 = 10

print(salto_de_linea(" Producto matricial "))
matriz1 = np.array([[1, 2],
                    [3, 4],
                    [5, 6]])

matriz2 = np.array([[1, 2, 3],
                    [3, 4, 5]])
print(f"Matriz 1: \n{matriz1}")
print(f"Matriz 2: \n{matriz2}")
print(f"Producto matricial: \n{matriz1 @ matriz2}")
