from sklearn import datasets
import numpy as np

iris = datasets.load_iris()
x = iris.data[:, [2,3]]
y = iris.target

print(f"Class labels: {np.unique(y)}")


# Division de los datos en entrenamiento y prueba
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size = 0.3, random_state = 1, stratify=y) # random_state es para que cada vez que se ejecute el código se obtenga la misma división de los datos, 
                                                        # stratify es para que la división de los datos sea proporcional a las clases

print("Conteo de labels en y:", np.bincount(y))
print("Conteo de labels en y_train:", np.bincount(y_train))
print("Conteo de labels en y_test:", np.bincount(y_test))