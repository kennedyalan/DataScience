# k vecinos cercanos
## ¿Qué es?
- Es un algoritmo que sirve para clasificar o predecir valores
- Es no parametrizado porque no se basa en una formula
- Memoriza el conjunto de entrenamiento y toma una decision cuando aparece una muestra nueva

## ¿Para qué sirve?
Se utiliza en **aprendizaje supervisado** para dos tareas:
- Clasificacion: Para asignar una categoria a un dato nuevo.
- Regresión: Para predecir un valor numerico o continuo.

## ¿Cómo funciona?
1. Elegir el valor de **"k"**: Elegir la cantidad de vecinos, que el algoritmo va a mirar para decidir
2. Calcular la **distancia**: Para saber quienes son los vecinos el algoritmo calcula que tan lejos estan los puntos entre sí.
3. **Voto mayoritario**: Una vez que identifica a los K vecinos se vota. Si la mayoria de esos k vecinos son de "clase a" entonces el algoritmo predice/clasifica que ese elemento será también de clase a. 

## Ventajas y desventajas
- Si se elige un K muy chico, el modelo se vuelve flexible pero puede captar ruido por outliers si elegís un K muy grande, las fronteras entre clases se vuelven más suaves pero el modelo puede volverse menos preciso
- Fundamental normalizar o estandarizar los datos, porque el algoritmo se basa en distancias.
- Como el algoritmo trabaja memorizando el dataset entero, este se vuelve lento con volumenes de datos gigantescos

## Tips
- **Evitar empates**: Si hay un numero de clases pares, elegir un k impar para evitar empates. Por ejemplo, "Clase Masculino", "clase femenino" 
- Cuidado con la **maldicion de la dimensionalidad**: No funciona bien cuando se tiene muchas caracteristicas. En espacios de alta dimensión, todos los puntos parecen estar lejos unos de otros
- **Algoritmos de busqueda**: Para datasets pequeños, el método de "fuerza bruta" es eficiente. Si tenés más de 30 muestras pero pocas dimensiones, KD-Tree es más rápido, mientras que Ball-Tree es mejor para datasets más grandes o complejos
