# -*- coding: utf-8 -*-
"""TP3kNN.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1exQOny8jzN6Xib8Mj-f3r-fgYOlOhJNq
"""

from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import time
import numpy as np
import seaborn as sns
from matplotlib.colors import ListedColormap
from sklearn import neighbors, datasets,metrics

info = digits.DESCR
info.split('\n')
"""
Taille du data set : 5620 instances 
Nombres de classes : 10
Nombres d'attribut : 64

"""

X_digits,Y_digits = load_digits(return_X_y=True)
X_digits = X_digits / X_digits.max()
X_train, X_test, y_train, y_test = train_test_split(
    X_digits, Y_digits, test_size=0.3, shuffle=False)

"""K = 3

"""

#K = 3 
start = time.time()
#distance
neigh = KNeighborsClassifier(n_neighbors=3)
print(neigh.fit(X_train,y_train))

y_pred = neigh.predict(X_test)
end = time.time()
accuracy = accuracy_score(y_test, y_pred, normalize=False)
rappel = recall_score(y_test,y_pred,average='macro')
fin = time.time()
print(f" Temps d'execution avec le fit : {end - start} secondes\n Temps d'execution avec le testing : {fin-start}\n Précision: {accuracy}\n Rappel: {rappel}")

#Pour le ploting nous utiliserons la matrice de confusion
disp = metrics.plot_confusion_matrix(neigh, X_test, y_test)
disp.figure_.suptitle("Confusion Matrix")
print(f"Confusion matrix:\n{disp.confusion_matrix}")

plt.show()

"""K = 1"""

#K = 1
start = time.time()
#distance
neigh = KNeighborsClassifier(n_neighbors=1)
print(neigh.fit(X_train,y_train))

y_pred = neigh.predict(X_test)
end = time.time()
accuracy = accuracy_score(y_test, y_pred, normalize=False)
rappel = recall_score(y_test,y_pred,average='macro')
fin = time.time()
print(f" Temps d'execution avec le fit : {end - start} secondes\n Temps d'execution avec le testing : {fin-start}\n Précision: {accuracy}\n Rappel: {rappel}")

disp = metrics.plot_confusion_matrix(neigh, X_test, y_test)
disp.figure_.suptitle("Confusion Matrix")
print(f"Confusion matrix:\n{disp.confusion_matrix}")

plt.show()

"""K = 5"""

#K = 5
start = time.time()
#distance
neigh = KNeighborsClassifier(n_neighbors=5)
print(neigh.fit(X_train,y_train))

y_pred = neigh.predict(X_test)
end = time.time()
accuracy = accuracy_score(y_test, y_pred, normalize=False)
rappel = recall_score(y_test,y_pred,average='macro')
fin = time.time()
print(f" Temps d'execution avec le fit : {end - start} secondes\n Temps d'execution avec le testing : {fin-start}\n Précision: {accuracy}\n Rappel: {rappel}")

disp = metrics.plot_confusion_matrix(neigh, X_test, y_test)
disp.figure_.suptitle("Confusion Matrix")
print(f"Confusion matrix:\n{disp.confusion_matrix}")

plt.show()

"""K = 7"""

#K = 7
start = time.time()
#distance
neigh = KNeighborsClassifier(n_neighbors=7)
print(neigh.fit(X_train,y_train))

y_pred = neigh.predict(X_test)
end = time.time()
accuracy = accuracy_score(y_test, y_pred, normalize=False)
rappel = recall_score(y_test,y_pred,average='macro')
fin = time.time()
print(f" Temps d'execution avec le fit : {end - start} secondes\n Temps d'execution avec le testing : {fin-start}\n Précision: {accuracy}\n Rappel: {rappel}")

disp = metrics.plot_confusion_matrix(neigh, X_test, y_test)
disp.figure_.suptitle("Confusion Matrix")
print(f"Confusion matrix:\n{disp.confusion_matrix}")

plt.show()