# -*- coding: utf-8 -*-
"""
Created on Sun Aug 21 20:44:51 2022

@author: Rabbi Amin
"""

planets = ['Mercury','Venus','Earth','Mars','Jupiter','Saturn','Uranus','Neptune','Pluto']
print("Before POP")
print(planets)
planets.pop()
print("After POP")
print( planets)

print("length of the list")
print(len(planets))

planets[2]="Our World"
print(planets)
print("Adding new value in the end ")
planets.append("Pluto")
print(planets)

print(planets.index("Venus"))#checking the index of vanues index start for 0

#convert numerator in ratio/denominator 
x = 0.125
print(x.as_integer_ratio())

