import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
from IPython.display import display


dataframe = pd.read_csv("https://raw.githubusercontent.com/mfares07/datascience/refs/heads/main/datasets/titanic_train.csv")
# Seleccion de datos con loc vs iloc

# loc: nombre de columnas
subset_loc = dataframe.loc[:4, ["Age", "Name", "Survived"]]

# iloc: indices, como dict (hashmap)
indices_columnas = [dataframe.columns.get_loc(c) for c in ["Age", "Name", "Survived", "Sex", "Fare"]]
subset_iloc = dataframe.iloc[:100, indices_columnas]

print(subset_loc)
print("---------------------------------------------------------------------------------------")
print(subset_iloc)