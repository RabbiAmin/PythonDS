# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 20:00:34 2022

@author: Rabbi Amin
"""

#KNNclassifier
#Import necessary python packages:
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
# download the iris dataset from its weblink 

path = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
#Assign column names to the dataset
headernames = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'Class']
#Read dataset to pandas dataframe 
dataset = pd.read_csv(path, names = headernames)
dataset.head()


#Data Preprocessing
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 4].values
# divide the data into 60% train and 40% test split. 
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.40)
# scaling the data
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)


# train the model with the help of KNeighborsClassifier class of sklearn 
from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors = 8)
classifier.fit(X_train, y_train)
# prediction
y_pred = classifier.predict(X_test)


# print the results 
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
result = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(result)
result1 = classification_report(y_test, y_pred)
print("Classification Report:",)
print (result1)
result2 = accuracy_score(y_test,y_pred)
print("Accuracy:",result2)
