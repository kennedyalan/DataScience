# Funciones
## Para crear una funcion se utiliza def, seguido del nombre y parentesis para pedir parametros.

def sumar(a, b):
    """Esta funcion toma dos numeros y los suma"""
    return a + b

# Funciones anonimas
## Para crear una funcion anonima se utiliza lambda, seguido de los parametros.
### lambda argumentos: expresion
saludar = lambda nombre: f"Hola {nombre}"

print(saludar(input("Ingrese su nombre: ")))


a = int(input("Ingrese un numero: "))
b = int(input("Ingrese otro numero: "))
print(f"La suma es {sumar(a, b)}")

## Ejercicio - escalado entre 0 y 1 (min max)
def escalado(datos):
    """"Esta funcion toma una lista de numeros y los escala entre 0 y 1"""
    min_dato = min(datos)
    max_dato = max(datos)
    return [(dato - min_dato) / (max_dato - min_dato) for dato in datos] # Usamos lista por comprension

print (escalado([10, 20, 30, 40, 50]))

# Lista por comprension: 
print([i for i in range(10)])


def escalar(datos):
    escalados = []
    min_dato = min(datos)
    max_dato = max(datos)

    for x in range(len(datos)):
        escalados.append((datos[x] - min_dato) / (max_dato - min_dato))
    
    return escalados
print(f"Datos escalados por mí: {escalar([10, 20, 30, 40, 50])}")

# Mutables e inmutables
# Strings, tuplas y numeros son inmutables, no se pueden modificar una vez creados.
# Listas, diccionarios y conjuntos son mutables, se pueden modificar una vez creados.   

# Funciones generadoras
def generador_pares(limite):
    num = 0
    while num < limite:
        yield num
        num += 2

pares = generador_pares(10)

## Con la palabra next() se obtiene el siguiente valor del generador. Se utiliza solo cuando se lo llama
for _ in range(5):
    try: 
        print(next(pares))
    except StopIteration:
        print("Se llegó al limite")