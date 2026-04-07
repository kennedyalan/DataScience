# Bucles

for i in range(5):
    print(i)

for i in "Hola a todos":
    print(i)

# Tuplas. Se pueden iterar
tupla = (1, 2, 3, 4, 5)
for numero in tupla:
    print(numero)

# Desempaquetar
tupla = (1, 2, 3)
a, b, c = tupla
print(a, b, c)

tupla2= (1, 2, 3, 4, 5)
try:
    a, b, c = tupla2
    print(a, b, c) # Esto dará error porque la tupla tiene más elementos que variables para desempaquetar
except ValueError as e:
    print("Error al desempaquetar:", e, "\n")

# Diccionarios. Se pueden iterar sobre las claves, valores o ambos
for dic in {"a": 1, "b": 2, "c": 3}:
    print(dic) # Imprime las claves

# Para iterar sobre los valores
for valor in {"a": 1, "b": 2, "c": 3}.values():
    print(valor)

# Otra forma, desempaquetar claves y valores
diccionario2 = {"a": 1, "b": 2, "c": 3}
for key, value in diccionario2.items():
    print(f"Clave: {key}, Valor: {value}")


# Otra forma
for d in diccionario2:
    print(d, diccionario2[d])

# Llenar una lista
lista = []
for i in range(0, 110, 10):
    lista.append(i)
    print(lista)

# Comprension de listas
lista = [i for i in range(0, 110, 10)] # Esto hace exactamente lo mismo que el bucle anterior pero de forma más concisa
print(lista)

