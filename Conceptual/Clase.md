# Análisis exploratorio
Lo primero que hacemos cuando vemos un conjunto de datos.
Vamos a ver si se puede hacer algo con esos datos y si tienen algun tipo de limite.

## Tipos
- Numéricos (7.3, 8, 13)
- Categóricos
    - Ordenables: ej. Universitario, Secundario, Primario
    - No ordenables: ej. Rojo, amarillo, verde

Parecidos: Podemos pensar en distancias. cual es la distancia entre alguien de un nivel economico A o B?. Cual es la distancia entre boca y river?.

Cuando esto no se puede deginir, no es ordenable proabablemente. Algunos algoritmos para cear modelos solo consumen datos numéricos
Debemos convertir el dato categorico al numerico.

vendemos equipos de buceo y queremos ver en que localidad vender: San antonio de areco: Puna a 4000 metros altura
San antonio oeste: Norte patagonia, bucear tiene sentido

Ordenar alfabeticamente en eset caso, van a estar muy cerca. Tiene sentido hacer esto en este caso? NO
No tiene sentido que la distancia sea tan cercana entre el primero, que esat en una montaña y el segundo que si tiene un lugar para bucear cercano

Cosas mal hechas:
- Enum para los nombres NO!!!
- Ordenar alfabeticamente y poner un numerito (MAL)

## Analisis individual
Extremos:
Media:
Mediana:
Desvio estandar.
Cuartiles:
- Moda: los que mas se repiten. por ej, talles de zapatos.
- Histograma: Podemos reflejar todo esto en un histograma

## Analisis individual categoricos: 
- Frecuencias
    - Absolutas:
    - Relativas: Proporción.
- Valores raros: Hinchas de sacachispas. Con estos valores. cuando un dato es verdadero, nunca lo sacamos. sacar un dato va a disminuir la variabilidad de la solucion. NUNCA sacar datos raros

## Correlaciones
### Entre numéricos
Cuando lo miramos de a dos, lo primero que miramos es la correlacion. Habla de que cuando crece uno crece el otro. Cuando decresce uno decresce el otro.
Cor()
Pairs()

### Entre datos categóricos
- Independencia de probabilidades: cuando uno de los datos no me trae info sobre el otro. alguien es hincha de talleres de cordoba. aporta info de que la probabilidad de que la persona sea cordobes?

### Entre numeros y categorias:
Nivel de estudios alcanzados (categoricos) y nivel de ingresos (numéricos)
- Boxplot en R
- Violin plot en python

## Reduccion de la dimensionalidad