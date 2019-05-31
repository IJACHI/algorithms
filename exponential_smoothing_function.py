# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 20:53:44 2018

@author: IJACH
"""
import random
import csv
from collections import defaultdict
from random import random,randint
import matplotlib.pyplot as plt
import numpy as np
#Function definitions

def exponential_smoothing(p, alpha):
    """This is exponential smoothing function """

    smoothed_price = [float(p[0])] # first value is same as series
    maximum=len(p)
    for n in range(0,maximum-1):
        # The next line populates the smoothed_price list with smoothed values using the stated relationship
        smoothed_price.append(alpha * p[n] + (1 - alpha) * smoothed_price[n])

    return smoothed_price

