# -*- coding: utf-8 -*-
"""
Created on Tue Oct 18 18:32:44 2022

@author: Rabbi Amin
"""

#import the libraries
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
#import matplotlib.pyplot as plt #Data Visualization 
#import seaborn as sns  #Python library for Vidualization
import csv
#import os

dataset = pd.read_csv('Mall_Customers.csv')

print(dataset.shape)