#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 00:46:27 2020

@author: simon
"""


import pandas as pd
from sklearn import preprocessing
import sklearn.model_selection as ms
from sklearn import linear_model
import sklearn.metrics as sklm
import numpy as np
import numpy.random as nr
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as ss
import math


AveMonthSpend_reduced = pd.read_csv('AveMonthSpend_reduced.csv')
AveMonthSpend_reduced.head(10)

aveSpend = AveMonthSpend_reduced['AveMonthSpend'].values 
indexes = np.where(aveSpend<84)[0]

delete_indexes = np.random.choice(indexes, size=int((1-25/75)*len(indexes)), replace=True, p=None)

AveMonthSpend_super_reduced = AveMonthSpend_reduced.drop(indexes, axis = 0)