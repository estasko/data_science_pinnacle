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
#%% Clean Data
# Cleaned data with no zero values for any row 
cleaned_data = data.query('Glucose !=0 & BloodPressure !=0 & SkinThickness' 
                          '!=0 & Insulin !=0')

#%% Plot Violin Plots
plt.figure(1, figsize = (8,6), clear = True)

subplot_num = 1

for key in dataframes:
    plt.subplot(2, 4, subplot_num)
    plt.title(f"{key} Distributions", size = 10)
    sns.violinplot(data = dataframes[key], y = key, x = 'Outcome')
    subplot_num +=1 

plt.tight_layout()

#%% Plot Scatter Plots

#Graph various variables vs. 2 Hour Serum Insulin 
plt.figure(2, clear = True)
plt.subplot(1,3, 1)

sns.scatterplot(x = 'BMI',
           y = 'Insulin',
           data = cleaned_data,
           hue = 'Outcome',
           size = 2)

plt.title('BMI vs. 2-Hour Serum Insulin')
plt.xlabel('BMI')
plt.ylabel('2-Hour Serum Insulin mu U/mL')

plt.subplot(1,3, 2)
sns.scatterplot(x = 'Glucose',
           y = 'Insulin',
           data = cleaned_data,
           hue = 'Outcome',
           size = 2)

plt.title('Glucose vs 2-Hour Serum Insulin')
plt.xlabel('Glucose')
plt.ylabel('2-Hour Serum Insulin mu U/mL')

plt.subplot(1,3, 3)
sns.scatterplot(x = 'Pregnancies',
           y = 'Insulin',
           data = cleaned_data,
           hue = 'Outcome',
           size = 2 )

plt.title('Pregnancies vs 2-Hour Serum Insulin')
plt.xlabel('Pregnancies')
plt.ylabel('2-Hour Serum Insulin mu U/mL')

#%% Exploring the Data
plt.figure(3, clear = True)
sns.histplot(cleaned_data,
             x = 'Insulin',
             hue = 'Outcome')
plt.title('2-Hour Insulin Serum by Diabetes Diagnosis')

plt.figure(4, clear = True)
sns.histplot(cleaned_data, 
              x = 'Age')
plt.title('Age of Participants in Dataset')

plt.figure(5, clear = True)
sns.histplot(cleaned_data, 
              x = 'Outcome',
              hue = 'Outcome',
              bins = 2)
plt.title('Diagnosis Count Among Participants')
