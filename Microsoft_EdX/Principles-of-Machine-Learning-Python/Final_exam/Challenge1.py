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
Test = pd.read_csv('TestSet.csv')
BikeBuyer = pd.read_csv('AW_BikeBuyer.csv')
print(AveMonthSpend.shape)
print(AveMonthSpend.CustomerID.unique().shape)

Demographics = pd.read_csv('AdvWorksCusts.csv')

birthdates = pd.to_datetime(Demographics['BirthDate'])
ages = (pd.to_datetime('1998-01-01')-birthdates)/np.timedelta64(1, 'Y')


Demographics["Ages"] = ages
age_group = ages.values

indexes_g1 = np.where(ages<25)[0]
indexes_g2 = np.where((ages>25)&(ages<45))[0]
indexes_g3 = np.where((ages>45)&(ages<55))[0]
indexes_g4 = np.where(ages>55)[0]


ages[indexes_g1] = "Group_1"
ages[indexes_g2] = "Group_2"
ages[indexes_g3] = "Group_3"
ages[indexes_g4] = "Group_4"

Demographics["AgeGroup"] = ages


Demographics["AveMonthSpend"] = AveMonthSpend['AveMonthSpend']


# Dealing with the number of cars
number_of_cars = Demographics["NumberCarsOwned"].copy()

indexes_g1 = np.where(number_of_cars ==0)[0]
indexes_g2 = np.where((number_of_cars>0)&(number_of_cars<3))[0]
indexes_g3 = np.where(number_of_cars>=3)[0]


number_of_cars[indexes_g1] = "No_car"
number_of_cars[indexes_g2] = "1-2"
number_of_cars[indexes_g3] = "3 or more"


Demographics["CarGroup"] = number_of_cars


# Dealing with the number of children

number_of_children = Demographics["NumberChildrenAtHome"].copy()


indexes_g1 = np.where(number_of_children ==0)[0]
indexes_g2 = np.where(number_of_children>=1)[0]


number_of_children[indexes_g1] = "No_children"
number_of_children[indexes_g2] = "With_Children"

Demographics["Childrens"] = number_of_children



# Adding the bike buyer
Demographics['Bikebuyer'] = BikeBuyer['BikeBuyer']



is_buyer = Demographics['Bikebuyer'] == 1

Demographics_buyers = Demographics[is_buyer]

cat_cols = [x  for x in Demographics.columns if pd.api.types.is_string_dtype(Demographics[x])]
#is_buyer = Demographics['Bikebuyer'] == 1
#count = [count + 1 for x in auto_prices[col] if x == '?']
