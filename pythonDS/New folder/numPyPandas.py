# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 12:31:26 2022

@author: Rabbi Amin
"""

#Importing and exporting a CSV

import pandas as pd
import numpy as np

music_data =  pd.read_csv("music.csv", header=0).values # If all of your columns are the same type:

print(music_data)

#also simply select the columns you need
x = pd.read_csv("music.csv", usecols=['Artist','Genre','Plays'])
print(x)

#a numpy array to import as pandas dataframe
#created array “a”
a = np.array([[-2.58289208,  0.43014843, -1.24082018, 1.59572603],
              [ 0.99027828, 1.17150989,  0.94125714, -0.14692469],
              [ 0.76989341,  0.81299683, -0.95068423, 0.11769564],
              [ 0.20484034,  0.34784527,  1.96979195, 0.51992837]])

dataFrm = pd.DataFrame(a) #assign Pandas Data frame to dataFem variable
print(dataFrm)
#save dataFrm as a csv file
dataFrm.to_csv('pandaDataFrame.csv')
np.savetxt('np.csv', a, fmt='%.2f', delimiter=',', header='1,  2,  3,  4')

#read 'pandaDataFrame.csv' file 
data = pd.read_csv('pandaDataFrame.csv')
print(data)