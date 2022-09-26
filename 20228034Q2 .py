# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 15:20:34 2022

@author: Md. Mohabbat HOSSAIN RUBEL
20228029
"""
import scipy.stats as ss
import numpy as np


x = [21.4, 19.7 ,19.7 ,20.6 ,20.8 ,20.1 ,19.7 ,20.3 ,20.9 ] #assign value
n= len(x) #length of n
xb= np.mean(x)
mu=20 #null hypothesis value
s = np.std(x)
#tcal, pval = ss.ttest_1samp(x, 20)
tcal = np.sqrt(n)*(xb-mu)/s 



alpha = 0.05 #for 95%confidance level

cvl = ss.t.ppf(alpha/2,n-1) #left tail
cvr = ss.t.ppf(1-alpha/2,n-1) #right tail
pval = 2*(1-ss.t.cdf(abs(tcal),n-1)) # calculating p value ,multiple by 2 for two sided


if tcal>cvr or tcal<cvl:
    print("Null Hypothesis is rejected at 5% level of significance")
else:
    print("Critical value approch")
    print("The null hypothesis is not rejected at 5% level of significance")
    

if pval < alpha:
    print("Null Hypothesis is rejected at 5% level of significance")
    
else:
    print("P_value approach ")
    print("The null hypothesis is not rejected at 5% level of significance")
