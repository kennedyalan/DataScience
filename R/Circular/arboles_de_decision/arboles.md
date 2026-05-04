# Arboles de decision:
Es un algoritmo que permite crear modelos de análisis **supervisado**. A partir de una muestra permite expandir ese resultado al resto.ç


Credito y solicitudes:
Universo: Creditos que me llegaran
Predecir quien me va a pagar y quien no

## ¿Como funciona?
Estructura de arbol, vamos a ir haciendo **preguntas** para separar
Con que pregunta empezar? La que separe mejor:
¿Alguna pregunta me separa en forma pura?

- Si la rta es SI la tomo, divido el problema y sigo analizando.
- Si la rta es NO entonces busco la division mas pura.
- Dependiendo de que consideramos pureza, surgen distintos algoritmos

Error esperado
CART
Ganancia de entropia
C4.5
DKM

## ¿Cuándo se termina?
- Esto de dividir y realizar preguntas se termina cuando me quedo sin atributos
Pueden surgir otros problemas:
Quizá no todas las divisiones sirven, pueden resultar caprichosas:
Por eso dividimos el conjunto inicial en dos partes:
- Entrenamiento 
- Validación

## Otros usos
Estimacion de valores o probabilidades
Para agrupamiento (OJOOO)

## Libreria en R:
RPART
