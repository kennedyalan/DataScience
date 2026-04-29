import pandas as pd

dataframe = pd.read_csv("https://raw.githubusercontent.com/mfares07/datascience/refs/heads/main/datasets/titanic_train.csv")

# A veces en algunos dataframes podemos tener columnas con datos categoricos, es decir, que no son numeros, sino que son palabras o etiquetas. 
# Por ejemplo, en un dataframe con columna "colores", podemos tener los valores "rojo", "verde" y "azul". 
# Para poder usar estos datos en modelos de machine learning, es necesario convertirlos a numeros.

# Pero que pasa si asignamos un numero a cada categoria? Por ejemplo, "rojo" = 1, "verde" = 2, "azul" = 3.
# El problema es que el modelo de machine learning puede interpretar que "verde" es mayor que "rojo" y que "azul" es mayor que "verde", lo cual no es cierto, porque son categorias sin orden.
# Para evitar esto, se utiliza la tecnica de hot encoding, que consiste en crear una columna para cada categoria, y asignar un 1 si la fila pertenece a esa categoria, y un 0 si no pertenece.

dummies_sex = pd.get_dummies(dataframe["Sex"], dtype=int)
print(dummies_sex.head(10))

dataframe = dataframe.join(dummies_sex)
dataframe = dataframe.drop(["Sex"], axis=1)

print(dataframe.head(10))

# Aca sex tenia dos categorias "male" y "female", entonces se crearon dos columnas
# Realmente necesitamos dos columnas? No, porque si en la columna female tenemos un 0 entonces sabemos que el sex es male
# Entonces podemos eliminar una de las columnas, por ejemplo la columna female y quedarnos solo con la columna male.
# Ejemplo con "Embarked"
dummies_embarked = pd.get_dummies(dataframe["Embarked"], dtype=int, drop_first=True, prefix="Embarked")
dataframe = dataframe.join(dummies_embarked)
dataframe = dataframe.drop(["Embarked"], axis=1)
print(dataframe.head(10))

# Finalmente, nos damos cuenta que. Si es Embarked_Q = 0 y Embarked_S = 0, entonces el valor de Embarked es C, entonces no necesitamos una columna para C.
