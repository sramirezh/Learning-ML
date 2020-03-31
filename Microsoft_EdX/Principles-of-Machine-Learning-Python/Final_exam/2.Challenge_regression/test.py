#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 18:21:09 2020

@author: simon
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import numpy.random as nr
import math
from sklearn import preprocessing
import sklearn.model_selection as ms
from sklearn import linear_model
import sklearn.metrics as sklm

BikeBuyer_reduced = pd.read_csv('BikeBuyer_reduced.csv')
BikeBuyer = pd.read_csv('AW_BikeBuyer.csv')

BikeBuyer.drop_duplicates(subset = 'CustomerID', keep = 'last', inplace = True)