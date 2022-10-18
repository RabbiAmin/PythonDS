# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 20:08:52 2022

@author: Rabbi Amin
"""

#knnregf.py
##KNN as Regressor
# importing necessary Python packages
import numpy as np
import pandas as pd
# download the iris dataset from its weblink 
path = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
# assign column names to the dataset 
headernames = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'Class']

# read dataset to pandas dataframe 
data = pd.read_csv(path, names = headernames)
array = data.values
X = array[:,:2]
Y = array[:,2]
data.shape

# import KNeighborsRegressor from sklearn to fit the model 
from sklearn.neighbors import KNeighborsRegressor
knnr = KNeighborsRegressor(n_neighbors = 10)
knnr.fit(X,Y)


# find the MSE as follows −
print ("The MSE is:",format(np.power(Y-knnr.predict(X),2).mean()))




#hh=knnr.predict(X)
#dd=X[1:10,]

#hh=knnr.predict(dd)
#import pandas as pd
#hhd=pd.DataFrame(hh)
#dd=X[1:10,]