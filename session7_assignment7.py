# -*- coding: utf-8 -*-
"""
Created on Sat Sep 15 18:10:51 2018

@author: disiz
"""
"""
Session 7
Assignment seven
"""
#Problem Statement
#Write a function to find moving average in an array over a window:
#Test it over [3, 5, 7, 2, 8, 10, 11, 65, 72, 81, 99, 100, 150] and window of 3.
#CODE FOR QUESTION 1
import numpy as np
x=np.array([3,5,7,2,8,10,11,65,72,81,99,100,150]) #given input list
N=3 #window
def movingAverage(x, N):  # defining function for calc moving average
    y = np.zeros((len(x)-N+1))
    for ctr in range(len(x)-N+1):
         y[ctr] = np.sum(x[ctr:(ctr+N)])
    return y/N
print("-"*80)
print("moving average output with given window is [rounded of to three digits] \n",np.round_(movingAverage(x,N),3))

print("-"*80)
print('\n')

print("\nEnd of assignment")