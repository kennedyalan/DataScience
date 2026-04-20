import pandas as pd

dataframe = pd.read_csv("https://raw.githubusercontent.com/mfares07/datascience/refs/heads/main/datasets/titanic_train.csv")

# Mirar las primeras filas
print(dataframe.head())
print("---------------------------------------------------------------------------------------")


# Mostrar todas las columnas
print(dataframe.columns)
print("---------------------------------------------------------------------------------------")

# Mostrar informacion del dataframe
print(dataframe.info())
print("---------------------------------------------------------------------------------------")

# Obtener el indice de una columna
print(dataframe.columns.get_loc("Embarked"))
print("---------------------------------------------------------------------------------------")

# Mostrar estadisticas claves
print(dataframe.describe())
print("---------------------------------------------------------------------------------------")

# Mostrar datos faltantes
print(dataframe.isna().sum())
print("---------------------------------------------------------------------------------------")

# Mostrar frecuencia de cada valor en una columna
print(dataframe["Pclass"].value_counts())
print("---------------------------------------------------------------------------------------")

# Mostrar datos random del dataframe
print(dataframe.sample(12))
print("---------------------------------------------------------------------------------------")