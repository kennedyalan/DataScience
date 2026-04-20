import seaborn as sb
import pandas as pd
import matplotlib.pyplot as plt

dataframe = pd.read_csv("https://raw.githubusercontent.com/mfares07/datascience/refs/heads/main/datasets/titanic_train.csv")

sb.countplot(x="Survived", data=dataframe)
sb.countplot(x="Survived", data=dataframe, hue="Pclass")
plt.show()

# Histogramas
dataframe.hist(figsize=(10, 5), bins=10, edgecolor="blue", grid=False)
plt.show()