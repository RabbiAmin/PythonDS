# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 20:27:17 2022

@author: Rabbi Amin
"""

def can_run_for_PM(age):
    return age>=30

print("Can 10 years old run for PM? ", can_run_for_PM(10))
print("can 40 years old run for PM?", can_run_for_PM(40))

#conditional operations if elif else
def value(x):
    if x == 0:
        print(x, "is zero")
    elif x > 0:
        print(x, "is positive")
    elif x < 0:
        print(x, "is negative")
    else:
        print(x, "is unlike anything I've ever seen...")

value(0)
value(-15)
value(15)
value(1)

#bollean operation convenstion 
print(bool(1))#true # all numbers and string is TRUE O and empty are False
print(bool(0))#false
print(bool())#flase
print(bool(""))#flase
print(bool("asdf"))#flase

#define a function called sign which takes a numerical argument and returns -1 if it's negative, 1 if it's positive, and 0 if it's 0.
def sign(x):
    if x == 0:
        return 0
    elif x < 0:
        return -1
    else:
        return 1