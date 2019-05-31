# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 19:21:00 2018

@author: IJACH
"""
import csv
from collections import defaultdict
import matplotlib.pyplot as plt
import numpy as np
from pylab import * 
import numpy as np 
import scipy.signal as sc 
import pandas as pd

print("Fast Fourier Transform (FFT) Algorithm")
print("................................")
print("This program uses the FFT algorithm to study cyclical movements \
      in stock price.")

# ------------ Let us check for existence of the file path -------------------------
check_filepath=True
while check_filepath:
    filepath=input('enter the path of the csv file with the stock price data \
                   WITHOUT any  quotations and press Enter: ')
# Example of a file path :  \Users\IJACH\Desktop\MSFE\PROGRAMMING IN PYTHON\FINAL PROJECT\MSFTDATA.csv

# the following try -except-else block catches the error in file path and allows for repeated attempt 
    try:
        f=csv.reader(filepath)
        print("Here is the filepath:"+ filepath) 
    except FileNotFoundError:
        print("The filepath doesn't exist or there are some missing directories , please check and try again")
    else:
        print("Great! the file path is correct. Now, you can carry on!")
        break
# ------------ Let us Open our data file -------------------------
columns = defaultdict(list) # each value in each column is appended to a list

file_handle=open('{}'.format(filepath),'r')
reader=csv.reader(file_handle,delimiter=",")
next(reader,None) # Skips the header of the file which is Time_Index and Adj_Close_Price

for row in reader :
    for (i,v) in enumerate(row):
        columns[i].append(v)

columns[0] = list(map(int, columns[0])) # This list corresponds to the time index
columns[1] = list(map(float, columns[1]))  # This list corresponds to the Adjusted closing price
time,price=columns[0],columns[1] # assigning the above values to a more intuitive name time for time and price for price
#print("Time index is {}".format(time))
#print("Adjusted closing prices are {} ".format(price))

file_handle.close()

np.count_nonzero(price) 
plt.plot(price) 
plt.title("Stock price movement")


#Python code
detrend=sc.detrend(price) 
#plt.plot(detrend) 
#plt.title("Stock detrended prices")


#Python code 
w=np.blackman(20) #we selected 20 the parameter of the blackman window function 
y=np.convolve(w/w.sum(),detrend,mode='same') 
plt.plot(y) 
plt.title("Blackman window function for detrended Stock price")


#Python code 
fft=abs(rfft(y)) 
plt.plot(fft) 
plt.title("FFT Algorithm applied to Stock price")
print (fft)
