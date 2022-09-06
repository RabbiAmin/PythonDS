# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 09:56:18 2022

@author: Rabbi Amin
"""

import numpy as np

#define 4*4 identity matrix 
I4 = np.eye(4) 
print("4*4 Identity Matrix: ")
print(I4)

#generate 4 random value and store it x, because for matrix multiplication
x = np.random.randn(4)
print("random number generated and store in x ")
print(x)

#matrix multiplication
print("I4 * x =")
print(np.dot(I4, x))

#import Liner Algebra ref: https://docs.scipy.org/doc/scipy/reference/linalg.html
import scipy.linalg as slin 

a = np.array([[ 3, -5, 8], [ -1, 2, 3], [ -5, -6, 2]]) #input a as array

# determination of the matrix
#A=[a b c
#   d e f
#   g h i]; det(A)= aei - afh- bdi + bfg + cdh - ceg
#for more check, https://www.studypug.com/linear-algebra-help/properties-of-determinants
d1= slin.det(a)
print('Determination of matrix "a" ')
print(d1)

#inverse of matrix
#for more about inverse matrix check, https://www.cuemath.com/algebra/inverse-of-a-matrix/
inverse = slin.inv(a)
print("Interse matrix of 'a' ")
print(inverse)
# numpy transpose , ref: https://numpy.org/doc/stable/reference/generated/numpy.transpose.html
tras = np.transpose(a)
print("Transpose 'a' ")
print(tras)

print(np.sum(a))

#15 elements in 3*5 array
a = np.arange(15).reshape(3, 5)
print("New 3*5 'a' array declier")
print(a)
print(a.shape)# shape of the array
a.dtype.name   #data type objec
a.ndim #Number of array dimensions
a.itemsize #itemsize will be 8, because this array consists of integers and size of integer (in bytes) is 8 bytes.
a.size #count the number of elements along a given axis
np.zeros((3, 4)) #creates an array full of zeros
np.ones((2, 3, 4), dtype=np.int16) #the function ones creates an array full of ones
np.empty((2, 3)) #the function empty creates an array whose initial content is random and depends on the state of the memory
np.arange(10, 30, 5) # create sequences of numbers
np.linspace(0, 2, 9) # here 9 is the how many element you want
a.sum() #all element of a addition
a.min() # find the min numb of a 
a.max() # find the maximum number of a 


#Mandelbrot set using matplotlib ref, https://en.wikipedia.org/wiki/Mandelbrot_set
import matplotlib.pyplot as plt

def mandelbrot(h, w, maxit=20, r=2):
    """Returns an image of the Mandelbrot fractal of size (h,w)."""
    x = np.linspace(-2.5,1.5, 5*h+2) #9
    y = np.linspace(-1.5, 1.5, 5*w+2) #7
    A,B= np.meshgrid(x,y) #used to create a rectangular grid out of two given one-dimensional arrays representing the Cartesian indexing or Matrix indexing
    C = A + B *1j
    z = np.zeros_like(C)
    divtime = maxit + np.zeros(z.shape, dtype =int)
                               
    for i in range(maxit):
        z = z**2 + C
        diverge = abs(z) > r # who is diverging
        div_now = diverge & (divtime == maxit)  # who is diverging now
        divtime[div_now] = i     # note when
        z[diverge] = r   # avoid diverging too much
    return divtime
        
plt.clf()
plt.imshow(mandelbrot(400, 400))


#Histograms
rg = np.random.default_rng(1) #construct a random number generator using default_rng
# Build a vector of 10000 normal deviates with variance 0.5^2 and mean 2
mu, sigma = 2, 0.5 # mean and standard deviation
v = rg.normal(mu, sigma, 10000) #normal distibution 
    #Verify the mean and the variance:
abs(mu - np.mean(v)) 
abs(sigma - np.std(v, ddof=1))   

# Plot a normalized histogram with 50 bins
plt.hist(v, bins=50, density=True) # matplotlib version (plot)
# Compute the histogram with numpy and then plot it
(n, bins) = np.histogram(v, bins=50, density=True)  # NumPy version (no plot)
plt.plot(.5 * (bins[1:] + bins[:-1]), n) 


import matplotlib.pyplot as plt2
# plot a new histogram 
count, bins, ignored = plt2.hist(v, 30, density=True)
plt2.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
               np.exp( - (bins - mu)**2 / (2 * sigma**2) ),
         linewidth=2, color='r')
plt2.show()
