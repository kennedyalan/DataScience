import numpy as np

def salto_de_linea(texto):
    return "=" * 20 + texto + "=" * 20

array_dimensiones = np.array([[1, 2, 3],
                              [4, 5, 6],
                              [7, 8, 9]])

print(salto_de_linea(" Acceso a elementos "))

print(array_dimensiones[0])     # Primera fila
print(array_dimensiones[2])     # Última fila
print(array_dimensiones[2, 2])  # Tercera fila, tercera columna
print(array_dimensiones[2][2])  # Ídem, forma alternativa
