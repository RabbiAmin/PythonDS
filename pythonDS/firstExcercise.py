# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 18:33:31 2022

@author: Rabbi Amin
"""
pi = 3.14159 # approximate
diameter = 3

# Create a variable called 'radius' equal to half the diameter
radius = diameter / 2
print(radius)

# Create a variable called 'area', using the formula for the area of a circle: pi times the radius squared
area = pi * radius ** 2  # one "*" for multi "**" for sqr
print (area)


#swap two variables using another variable 
a = [1, 2, 3]
b = [3, 2, 1]
tmp = a
a = b
b = tmp

#a, b = b, a
print(a,b)