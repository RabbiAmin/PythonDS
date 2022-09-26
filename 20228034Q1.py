# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 15:15:02 2022

@author: Md. Rabbi Amin
20228034
"""
import pandas as pd
import numpy as np
from scipy.stats import skew

data = {"year" :[2011,2012,2010],
        "team" :["RMadrid","Rmadrid","ValnciaCF"],
        "wins" :[32,26,21],
        "draws":[2,5,9]
        }
df = pd.DataFrame(data)
variance = np.var(df["wins"])
skewness = skew(df["wins"])
