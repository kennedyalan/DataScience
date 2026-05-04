import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, accuracy_score

clientes_credito = pd.read_csv('Data/Clientes_Credito.csv', sep=';')

clase = clientes_credito['Buen Pagador']
datos = clientes_credito[['Monto Credito', 'Ingreso Neto', 'Coeficiente Credito', 'Monto Cuota', 'Grado Academico']]

escalador = preprocessing.StandardScaler()
datos = escalador.fit_transform(datos)

# Primero probamos con K=3
clasificador = KNeighborsClassifier(n_neighbors=3)
clasificador.fit(datos, clase)

nuevos_clientes = np.array([
    [4, 4, 2, 2, 3],
    [1, 4, 3, 2, 4],
    [3, 2, 3, 4, 2],
    [4, 1, 3, 3, 2],
    [3, 4, 3, 1, 3],
    [1, 3, 2, 2, 4],
    [3, 3, 3, 3, 1],
])

nuevos_clientes = escalador.transform(nuevos_clientes)
predicciones = clasificador.predict(nuevos_clientes)

for i, pred in enumerate(predicciones):
    print(f"Cliente {100 + i}: {pred}")

clase_np = np.array(clase)

plt.scatter(datos[clase_np == 0, 0], datos[clase_np == 0, 1],
            c='red', edgecolor='k', s=100, label='Mal Pagador')
plt.scatter(datos[clase_np == 1, 0], datos[clase_np == 1, 1],
            c='blue', edgecolor='k', s=100, label='Buen Pagador')
plt.scatter(nuevos_clientes[:, 0], nuevos_clientes[:, 1],
            c='green', edgecolor='k', s=200, marker='X', label='Nuevos Clientes')
plt.xlabel('Monto Credito (escalado)')
plt.ylabel('Ingreso Neto (escalado)')
plt.legend()
plt.show()

# Probamos con K=5
clasificador_k5 = KNeighborsClassifier(n_neighbors=5)
clasificador_k5.fit(datos, clase)
predicciones_k5 = clasificador_k5.predict(nuevos_clientes)
print("\nPredicciones con K=5:")
for i, pred in enumerate(predicciones_k5):
    print(f"Cliente {100 + i} con K=5: {pred}")

datos_train, datos_test, clase_train, clase_test = train_test_split(
    datos, clase, test_size=0.3, random_state=1, stratify=clase)

for k in [3, 5]:
    clasiffier = KNeighborsClassifier(n_neighbors=k)
    clasiffier.fit(datos_train, clase_train)
    predicciones_test = clasiffier.predict(datos_test)

    accuracy = accuracy_score(clase_test, predicciones_test)
    print(f'Accuracy para K={k}: {accuracy:.2f}')
    cm = confusion_matrix(clase_test, predicciones_test)
    display = ConfusionMatrixDisplay(cm, display_labels=clasiffier.classes_)
    display.plot()
    plt.title(f'Matriz de Confusión para K={k}')
    plt.show()