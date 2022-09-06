# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 09:56:18 2022

@author: Rabbi Amin
"""

import numpy as np

#define 4*4 identity matrix 
I4 = np.eye(4) 
print(I4)

x = np.random.randn(4)
print(x)

print(np.dot(I4, x))