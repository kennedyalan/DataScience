import numpy as np

def salto_de_linea(texto):
    return "=" * 20 + texto + "=" * 20

array_ejemplo = np.array([[[3, 6, 9], [12, 15, 18]],
                          [[21, 24, 27], [30, 33, 36]],
                          [[39, 42, 45], [48, 51, 54]]])

print(salto_de_linea(" Ordenar, agregar y borrar elementos "))
print(np.sort([2, 1, 5, 3, 7, 4, 6, 8]))

array_ordenado = np.sort(array_ejemplo)
print(f"Array ordenado: \n{array_ordenado}")
print(f"Array en orden inverso: \n{array_ordenado[::-1]}")
