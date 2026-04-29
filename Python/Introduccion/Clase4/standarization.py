def calcular_media(lista):
    return sum(lista) / len(lista)

def calcular_desviacion(lista):
    return (sum((x - calcular_media(lista)) ** 2 for x in lista) / len(lista)) ** 0.5 # Expresion generadora, en este caso sum llama al generador

def estandarizar(lista):
    media = calcular_media(lista)
    desviacion = calcular_desviacion(lista)

    return [(round((x - media) / desviacion, 2)) for x in lista] # Comprension de listas

lista = [5, 7, 10, 12, 15, 18, 20]
print(calcular_media(lista))
print(calcular_desviacion(lista))
print(estandarizar(lista))