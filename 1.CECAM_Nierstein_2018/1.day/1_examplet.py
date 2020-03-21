#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 15:39:20 2018

@author: simon
"""

import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf

# Choose datasets using 

(train,label_train), (test, label_test) = tf.keras.datasets.mnist.load_data() #Labeled digits
(train,label_train), (test, label_test) = tf.keras.datasets.fashion_mnist.load_data() #Labeled clothe

print (train.shape, test.shape)
print (train.dtype)