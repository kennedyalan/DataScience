import pandas as pd

dataframe = pd.read_csv("https://raw.githubusercontent.com/mfares07/datascience/refs/heads/main/datasets/titanic_train.csv")

# Age tiene datos faltantes
edades_faltantes = dataframe["Age"].isna().sum()
print(f"Datos faltantes en Age: {edades_faltantes}")

# Imputar datos (rellenar los datos faltantes con un valor, en general, la media)
# Calcular la edad media del dataframe
edad_media = dataframe["Age"].mean()

# Rellenar
dataframe["Age"] = dataframe["Age"].fillna(edad_media)

# Cuantos datos faltantes hay ahora?
print(f"Datos faltantes en Age después de imputar: {dataframe['Age'].isna().sum()}")

# Nota: No siempre esta bueno imputar datos, siempre depende
# Supongamos que tenemos una columna que se trata de altura de la marea
# Si tenemos datos faltantes, no es buena idea imputar con la media, porque la altura de la marea puede variar mucho dependiendo del día, 
# entonces no es buena idea imputar con la media, porque no es representativo. En ese caso, lo mejor sería interpolar los datos faltantes, es decir, 
# usar los datos anteriores y posteriores para estimar el valor faltante.

# Eliminar columna Cabin
print(f"Datos faltantes en Cabin: {dataframe['Cabin'].isna().sum()}")
dataframe = dataframe.drop(["Cabin"], axis=1)

# Eliminar filas con datos faltantes
dataframe = dataframe.dropna()

