# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 18:05:54 2022

@author: Rabbi Amin
"""
import pandas as pd

titanic_data = pd.read_csv("titanic_data.csv")

titanic_data.head()

#tatal pesengers 
total = len(titanic_data)
print(total)


#survived pesengers
survived = (titanic_data.Survived == 1). sum()
print(survived)


#minors pesenger
minor = (titanic_data.Age < 18). sum()
print(minor)
