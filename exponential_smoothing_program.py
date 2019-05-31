# -*- coding: utf-8 -*-
"""
Created on Sun Apr  8 19:21:00 2018

@author: IJACH
"""
import csv
from collections import defaultdict
from random import random,randint
import matplotlib.pyplot as plt
import numpy as np
import exponential_smoothing_function
import regression_function

print("Program: Exponential Smoothing and Linear Regression Forecast")
print("............................................................")
print("This program uses exponential smoothing to help predict a value \
      in the future. In addition, it also comes up with the linear \
      regression equation to predict the same  value as was done in \
      exponential smoothing.")

# ------------ Let us check for existence of the file path -------------------------
check_filepath=True
while check_filepath:
    filepath=input('enter the path of the csv file with the stock price data     WITHOUT any  quotations and press Enter: ')
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
t,p=columns[0],columns[1] # assigning the above values to a more intuitive name t for time and p for price
print("Time index is {}".format(t))
print("Adjusted closing prices are {} ".format(p))
file_handle.close()

#------------------ Let us do the exponential smoothing part now ----------------
exponential_smoothed_price = exponential_smoothing_function.exponential_smoothing
"""def exponential_smoothing(original_series, alpha):
    smoothed_price = [float(original_series[0])] # first value is same as series
    maximum=len(original_series)
    for n in range(0,maximum-1):
        # The next line populates the smoothed_price list with smoothed values using the stated relationship
        smoothed_price.append(alpha * original_series[n] + (1 - alpha) * smoothed_price[n])

    return smoothed_price

original_series=p """



#-------- model parameter selection -----------
def find_the_right_alpha():
    original_series=p

    while True:              # keep looping until `break` statement is reached
        alpha_value=float(input("Enter a number between 0 exclusive and 1 inclusive: "))
        try:                 # get ready to catch exceptions inside here
            if 0.0 < alpha_value <= 1.0:

                y=exponential_smoothed_price(p,alpha_value) # y is another name for smoothed_price
                y = [ round(elem, 2) for elem in y ] # rounding off the y values to 2 significant digits
                print("The smoothed values of the price are {}".format(y))
                        #------------ Plotting time --------------

                plt.plot(t,y,label='Smoothed data',c='r')
                plt.xlabel('Time Index')
                plt.ylabel('Prices')
                plt.plot(t,original_series,label='Original data',c='b')

                plt.grid(True)
                plt.legend()
                plt.show()
                response=input("Do you like the smoothed data ? Enter Y for yes: ")
                # --------checking if the user is happy with the selection of alpha -----------
                if (response =='Y' or response=='y'):
                    print("Great! You seem to be satisfied with alpha value of {}".format(alpha_value))
                    break
                else:
                # This block would give the chosen alpha value as it wouldn't be 
                #executed after the final decision of choice is made
                    alpha_value=find_the_right_alpha() 
                    break
            else:
                print(" Let us try again!")
        except ValueError:      # <-- exception. handle it. loops because of while True
            print("Not a valid alpha value, let's try that again")
    return alpha_value

#---------- End of find_the_right_alpha function-----------------


alpha_value=find_the_right_alpha() # function call to determine alpha

t_predict=len(t)-1
def smoothing_predict(t_predict):
    y=exponential_smoothed_price(p,alpha_value)
    smooth_predicted=round((alpha_value*p[t_predict]+ (1-alpha_value)*y[t_predict]),3)
    display_value=print(" The smoothing predicted value for time {} is {}".format(t_predict+2,smooth_predicted))
    return display_value

smoothing_predict(t_predict)

# -------------- Regression time--------------
"""
mean = regression_function.calc_mean
coefficients = regression_function.calc_coefficients
regression_line = regression_function.graph_regression_line
regression_formula = regression_function.regression_formula
r_square = regression_function.calc_r_square
regression_predict = regression_function.regression_predict
"""


def calc_mean(t):
    total_sum=0
    for i in range(0,len(t)):
        total_sum+=t[i]
        result=total_sum/len(t)
    return result

def calc_coefficients(t,p):

    sum_xy_deviation=0
    sum_xsquared_deviation=0


    for i in range(0,len(t)):
        sum_xy_deviation+=(t[i]-calc_mean(t))*(p[i]-calc_mean(p))

        sum_xsquared_deviation+=pow(t[i]-calc_mean(t),2)

    beta=float(sum_xy_deviation/sum_xsquared_deviation)
    alpha=calc_mean(p)-beta*calc_mean(t)
    coefficients={'alpha':round(alpha,3), 'beta':round(beta,3)}
    return coefficients

def graph_regression_line(regression_formula,t):
    t=np.array(t)
    phat=regression_formula(t)
    plt.title('Regression Line and original data scatter plot')
    plt.scatter(t, p,c='b')
    plt.plot(t,phat)
    plt.show()

def regression_formula(t):
    coefficients=calc_coefficients(t,p)
    return coefficients['alpha']+t*coefficients['beta']
def calc_r_square(t,p):
    SSR,SST=0,0 # SSR is regression sum of squares. SST is total sum of squares
    p_hat=[]
    mean_price=calc_mean(p)
    coefficients=calc_coefficients(t,p)
    for i in range(0,len(t)):
        p_hat.append(coefficients['alpha']+coefficients['beta']*t[i])
        SSR+=pow(p_hat[i]-mean_price,2)
        SST+=pow(p[i]-mean_price,2)
    r_squared=round(SSR/SST,3)
    display_value=print(" The R-Squared value  is {}".format(r_squared))
    return display_value

t_predict=len(t)-1
def regression_predict(t_predict):
    coefficients=calc_coefficients(t,p)
    predicted=round((coefficients['alpha']+t_predict*coefficients['beta']),3)
    display_value= print(" The regression predicted value for time {} is {}".format(t_predict+2,predicted))
    return display_value

#-----------------------Displaying the output of our regression analysis --------------
graph_regression_line(regression_formula,t)
print("\n")
calc_r_square(t,p)
print("\n")
regression_predict(t_predict)
print("----------------")
print("The actual predicted value for time 9 is 3.32")
print("----------------")