#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 15:16:40 2020
First challenge 
@author: simon
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import numpy.random as nr
import math


AveMonthSpend = pd.read_csv('AW_AveMonthSpend.csv')
TestSet = pd.read_csv('AW_test.csv')
print(AveMonthSpend.shape)
print(AveMonthSpend.CustomerID.unique().shape)

# For the test set
print(TestSet.shape)
print(TestSet.CustomerID.unique().shape)

AveMonthSpend.drop_duplicates(subset = 'CustomerID', keep = 'last', inplace = True)
print(AveMonthSpend.shape)
print(AveMonthSpend.CustomerID.unique().shape)
BikeBuyer = pd.read_csv('AW_BikeBuyer.csv')
BikeBuyer.head(40)


BikeBuyer.drop_duplicates(subset = 'CustomerID', keep = 'last', inplace = True)
print(BikeBuyer.shape)
print(BikeBuyer.CustomerID.unique().shape)

Demographics = pd.read_csv('AdvWorksCusts.csv')
Demographics.head(5) # TBH here is better to open the data or use spyder


print(Demographics.shape)
print(Demographics.CustomerID.unique().shape)

Demographics.drop_duplicates(subset = 'CustomerID', keep = 'last', inplace = True)
print(Demographics.shape)
print(Demographics.CustomerID.unique().shape)

# Adding the BikeBuyer
Demographics['Bikebuyer'] = BikeBuyer['BikeBuyer']
# Adding the AveMonthSpend
Demographics["AveMonthSpend"] = AveMonthSpend['AveMonthSpend']


# Operating on the training set
birthdates = pd.to_datetime(Demographics['BirthDate'])
ages = (pd.to_datetime('1998-01-01')-birthdates)/np.timedelta64(1, 'Y')
Demographics["Ages"] = ages # Adding the new column


# Operating on the test set
test_birthdates = pd.to_datetime(TestSet['BirthDate'])
test_ages = (pd.to_datetime('1998-01-01')-test_birthdates)/np.timedelta64(1, 'Y')
TestSet["Ages"] = test_ages # Adding the new column


def group_ages(df):

    ages_series = Demographics["Ages"].copy()
    ages = ages_series.values

    ages_groups = ages_series.astype(str)

    groups = ages_groups.values


    indexes_g1 = np.where(ages<25)[0]
    indexes_g2 = np.where((ages>25)&(ages<45))[0]
    indexes_g3 = np.where((ages>45)&(ages<55))[0]
    indexes_g4 = np.where(ages>55)[0]



    groups[indexes_g1] = "Group_1"
    groups[indexes_g2] = "Group_2"
    groups[indexes_g3] = "Group_3"
    groups[indexes_g4] = "Group_4"
    
    return groups


Demographics["AgeGroup"] = group_ages(Demographics)

