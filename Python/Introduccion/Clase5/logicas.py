import numpy as np

def salto_de_linea(texto):
    return "=" * 20 + texto + "=" * 20

print(salto_de_linea(" Logicas "))
ar = np.arange(5, 20)
print(f"Array: \n{ar}")

print(ar[ar > 10])

mayores_que_10 = ar[ar > 10]
print(f"Mayores que 10: \n{mayores_que_10}")

print(f"Mayores que 5 y pares: \n{ar[(ar > 5) & (ar % 2 == 0)]}")
