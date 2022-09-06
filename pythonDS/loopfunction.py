# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 18:30:08 2022

@author: Rabbi Amin
"""
import math 
def sqfun(x):
    return x*x

sqfun(3) #passing value 3 for sqfun and it return 9

a=[5,6,9,1,4,1,6]
n= len(a) #assign the length size in n, here it is 7

sum = 0
i = 0
while (i < (n-1)): #while loop for a[0] to a[6] adding 
    sum = sum + a[i]
    print(sum)
    i=i+1
#for loop for printing sum of the array  
sum2 = 0
for i in range (0, n-1, 1):
    sum2 = sum2 + a[i]
    print(i, sum2)

#Mean calculation
"Mean=",sum/n
meanManualy = sum/n

#Variance Calculation

sum3=0
for i in range (0, n-1, 1):
    sum3 = sum3 + (a[i]-meanManualy)**2
    print(i,sum3)
"Variance=",sum3/(n-1)
var = sum3/(n-1)
print(var)


import numpy as np

#standard deviation
stdDev = np.sqrt(var)
print(stdDev)