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
print(AveMonthSpend.shape)
print(AveMonthSpend.CustomerID.unique().shape)

Demographics = pd.read_csv('AdvWorksCusts.csv')