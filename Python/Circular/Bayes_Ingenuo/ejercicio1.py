import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

historical_clients = pd.read_csv('../Data/Datos_Historicos_Clientes.csv', sep = ";")
new_clients = pd.read_csv('../Data/Nuevos_Clientes.csv', sep = ";")

# Limpiar datos y convertir variables categóricas a numéricas
historical_clients = pd.get_dummies(historical_clients, columns=['EstadoCivil', 'Profesion'])
historical_clients["Universitario"] = historical_clients["Universitario"].map({'Si': 1, 'No': 0})
historical_clients["TieneVehiculo"] = historical_clients["TieneVehiculo"].map({'Si': 1, 'No': 0})
historical_clients["Compra"] = historical_clients["Compra"].map({'Si': 1, 'No': 0})

new_clients = pd.get_dummies(new_clients, columns=['EstadoCivil', 'Profesion'])
new_clients["Universitario"] = new_clients["Universitario"].map({'Si': 1, 'No': 0})
new_clients["TieneVehiculo"] = new_clients["TieneVehiculo"].map({'Si': 1, 'No': 0})

# Bayes ingenuo requiere que las columnas de caracteristicas esten separadas de la respuesta
X = historical_clients.drop(columns=['IdCliente', 'Compra'])
y = historical_clients['Compra']

X_new = new_clients.drop(columns=['IdCliente', 'Compra'])
# Asegurarse de que las columnas de nuevos clientes coincidan con las de los clientes historicos, 
# ya que get_dummies puede crear columnas diferentes
X_new = X_new.reindex(columns=X.columns, fill_value=0)

modelo = GaussianNB()
modelo.fit(X, y)