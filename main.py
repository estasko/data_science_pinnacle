#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 26 14:48:37 2025

@author: abbyhoward
"""

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
#%%
# Read in the dataset
data = pd.read_csv('Healthcare-Diabetes.csv', index_col= 'Id')

#check for na 
data.isna().any()
#%%
# See how many zero counts for each column
(data == 0).sum()

#%% 
# For data analysis, create DataFrames for each variable against outcome,
# removing zero values to assess trends via violin plots
        
dataframes = {} 

for col in data:
    if col == 'Pregnancies':
        dataframes[col] = data.loc[:, (col, 'Outcome')]
    if col == 'Outcome':
        pass
    else:
        dataframes[col] = data.loc[:, (col, 'Outcome')].query('`{}` != 0'.format(col))

dataframes['Pregnancies'].head()
#%%
# Cleaned data with no zero values for any row 
cleaned_data = data.query('Glucose !=0 & BloodPressure !=0 & SkinThickness' 
                          '!=0 & Insulin !=0')
#%%
plt.figure(1, clear = True)

subplot_num = 1

for key in dataframes:
    plt.subplot(2, 4, subplot_num)
    plt.title(f"{key} as Predictor for Diabetes Outcome", size = 10)
    sns.violinplot(data = dataframes[key], y = key, x = 'Outcome')
    subplot_num +=1 

plt.tight_layout()

#%%

# Compare age and glucose against outcome 

preg_glucose = data.loc[:,('Pregnancies', 'Glucose', 'Outcome')].query('Glucose !=0')
plt.figure(2, clear = True)
sns.violinplot(data=preg_glucose, x = 'Pregnancies', y = 'Glucose', hue = 'Outcome', split = True)


preg = pd.cut(data.loc[:,'Pregnancies'], 5,
       # labels=["group 1", "group 2", "group 3", "group 4", "group 5"]
       )

preg_glucose = pd.DataFrame(data = {"Pregnancies": preg,
                                    "Glucose": data.loc[:,('Glucose')],
                                    "Outcome": data.loc[:,('Outcome')]
                                                           })
plt.figure(3, clear = True)
sns.violinplot(data=preg_glucose, x = 'Pregnancies', y = 'Glucose', hue = 'Outcome')




