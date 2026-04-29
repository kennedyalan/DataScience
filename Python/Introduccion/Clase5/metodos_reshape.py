import numpy as np

def salto_de_linea(texto):
    return "=" * 20 + texto + "=" * 20

array_ejemplo = np.array([[[3, 6, 9], [12, 15, 18]],
                          [[21, 24, 27], [30, 33, 36]],
                          [[39, 42, 45], [48, 51, 54]]])

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
