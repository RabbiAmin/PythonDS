# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 18:51:56 2022

@author: Rabbi Amin
"""

def least_difference(a, b, c):
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(a - c)
    return min(diff1, diff2, diff3)

def heighest_difference(a, b, c):
    diff1 = abs(a - b)
    diff2 = abs(b - c)
    diff3 = abs(a - c)
    return max(diff1, diff2, diff3)
    

print(
    least_difference(1, 10, 100),
    least_difference(1, 10, 10),
    least_difference(5, 6, 7), # Python allows trailing commas in argument lists. How nice is that?
)

help(least_difference)

print(least_difference(2, 5, 9))# -3 -4 -7
print(heighest_difference(2, 5, 9))


#adding optional arguments with default value
def greet(who="Amin"):
    print("Hello,", who)
    
greet()
greet(who="Himel")
# (In this case, we don't need to specify the name of the argument, because it's unambiguous.)
greet("world")


#function applied function
def mul_by_four(x):
    return 4 * x

def first_function_call(ff, arg):
    print("first argument works.")
    return ff(arg)

def second_function_call(ff, arg):
    print("Second argument call. ")
    return ff(ff(arg))

print(first_function_call(mul_by_four, 2))
print(second_function_call(mul_by_four, 2))
    