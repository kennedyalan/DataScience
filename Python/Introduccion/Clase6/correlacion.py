import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

dataframe = pd.read_csv("https://raw.githubusercontent.com/mfares07/datascience/refs/heads/main/datasets/titanic_train.csv")

dummies_sex = pd.get_dummies(dataframe["Sex"], dtype=int)

dataframe = dataframe.join(dummies_sex)
dataframe = dataframe.drop(["Sex"], axis=1)


dummies_embarked = pd.get_dummies(dataframe["Embarked"], dtype=int, drop_first=True, prefix="Embarked")
dataframe = dataframe.join(dummies_embarked)
dataframe = dataframe.drop(["Embarked"], axis=1)


# Matriz de correlación:
# La matriz de correlación es una tabla que muestra la correlación entre todas las variables numéricas de un dataframe.
# La correlación es una medida de la relación entre dos variables, y puede ser positiva, negativa o nula. La correlación positiva indica que a medida que una variable aumenta, la otra también aumenta. 
# La correlación negativa indica que a medida que una variable aumenta, la otra disminuye. La correlación nula indica que no hay relación entre las variables.
# Por ejemplo: dataframe inmobiliario de casas: distancia entre la costa y precio
# A medida que la distancia se acorta, el precio de la casa aumenta.
# Ejemplo 2: Peso y altura de una persona: a medida que la altura aumenta, el peso también aumenta.

plt.figure(figsize=(8, 8))
sb.heatmap(dataframe.select_dtypes(include='number').corr(), annot=True, cmap="inferno", cbar=True)
plt.show()