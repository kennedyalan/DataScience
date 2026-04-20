import pandas as pd

dataframe = pd.read_csv("https://raw.githubusercontent.com/mfares07/datascience/refs/heads/main/datasets/titanic_train.csv")

dataframe["Family_size"] = dataframe.apply(
    lambda row: row["SibSp"] + row["Parch"] + 1,
    axis=1
)

dataframe.sample(8)

# Esto es un ejemplo de apply() pero esto es mas eficiente:
dataframe["Family_size"] = dataframe["SibSp"] + dataframe["Parch"] + 1
dataframe.sample(8)