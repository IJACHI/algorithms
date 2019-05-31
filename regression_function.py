# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 22:40:09 2018

@author: IJACH
"""

import random
import csv
from collections import defaultdict
from random import random,randint
import matplotlib.pyplot as plt
import numpy as np

#Function definitions


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

