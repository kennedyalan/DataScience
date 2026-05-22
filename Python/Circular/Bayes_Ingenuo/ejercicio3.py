from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix, precision_score, roc_curve, auc
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

dataset = datasets.load_breast_cancer()
print(dataset)


print('Información en el dataset:' + str(dataset.keys()))


print('Descripción del dataset:' + str(dataset['DESCR']))

# Seleccionar las características y la variable objetivo
X = dataset.data
y = dataset.target

# Spliteo teset y train
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Entrenamiento
algoritmo = GaussianNB()
algoritmo.fit(X_train, y_train)

# Predicción
y_pred = algoritmo.predict(X_test)



# Resultados
matriz = confusion_matrix(y_test, y_pred)
precision = precision_score(y_test, y_pred)


print('Matriz de Confusión:')
print(matriz)


print('Precisión del modelo:')
print(precision)


plt.figure(figsize=(6, 5))
sns.heatmap(matriz, annot=True, fmt='d', cmap='Blues',
            xticklabels=dataset.target_names,
            yticklabels=dataset.target_names)
plt.xlabel('Predicción')
plt.ylabel('Real')
plt.title('Matriz de Confusión')
plt.tight_layout()
plt.show()


y_prob = algoritmo.predict_proba(X_test)[:, 1]
fpr, tpr, _ = roc_curve(y_test, y_prob)
roc_auc = auc(fpr, tpr)

plt.figure(figsize=(6, 5))
plt.plot(fpr, tpr, color='darkorange', lw=2, label=f'AUC = {roc_auc:.2f}')
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlabel('Tasa de Falsos Positivos')
plt.ylabel('Tasa de Verdaderos Positivos')
plt.title('Curva ROC')
plt.legend(loc='lower right')
plt.tight_layout()
plt.show()


medias_maligno = X_train[y_train == 0].mean(axis=0)
medias_benigno = X_train[y_train == 1].mean(axis=0)
diferencias = np.abs(medias_maligno - medias_benigno) / (X_train.mean(axis=0) + 1e-9)
top_indices = np.argsort(diferencias)[-10:][::-1]
top_features = [dataset.feature_names[i] for i in top_indices]

x = np.arange(len(top_features))
width = 0.35

plt.figure(figsize=(12, 5))
plt.bar(x - width/2, medias_maligno[top_indices], width, label='Maligno', color='salmon')
plt.bar(x + width/2, medias_benigno[top_indices], width, label='Benigno', color='steelblue')
plt.xticks(x, top_features, rotation=45, ha='right')
plt.title('Top 10 Features: Media por Clase')
plt.ylabel('Valor medio')
plt.legend()
plt.tight_layout()
plt.show()


# b) Los datos que toma el ejemplo es del dataset breast cancer
# c) Se interpreta que el modelo tiene precision de 97% para este dataset. Predijo 3 veces que era maligno cuando era benigno
# Predijo 2 veces que era benigno cuando era maligno. El modelo es muy bueno para este dataset. 