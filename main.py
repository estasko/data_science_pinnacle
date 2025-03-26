#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 26 14:48:37 2025

@author: abbyhoward
"""

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
#%%
#read in dataset
data = pd.read_csv('Healthcare-Diabetes.csv', index_col= 'Id')

#check for na 
data.isna().any()
#%%
#see how many zero counts for each column
(data == 0).sum()
