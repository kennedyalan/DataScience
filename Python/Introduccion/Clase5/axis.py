import numpy as np

def salto_de_linea(texto):
    return "=" * 20 + texto + "=" * 20

print(salto_de_linea(" Axis "))
array_axis = np.array([[1, 2, 3],
                       [1, 2, -2]])

print(f"Array original: \n{array_axis}")
print(f"Suma por columnas (axis=0): \n{array_axis.sum(axis=0)}")
print(f"Suma por filas (axis=1): \n {array_axis.sum(axis=1)})")
