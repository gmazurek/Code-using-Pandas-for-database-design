#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created on Tue Feb 19 11:56:25 2019

@author: gabriellamazurek
"""

import pandas as pd
import numpy as np


def pandas1():
    #read in the csv and account for the missing data with asterisks. Note: in assignment #2 I did not have asterisks in place of missing data, and now I do.
    df=pd.read_csv(' data_out_copy.csv',sep=',',encoding='utf-8',
                na_values='*')
   
    #get number of rows and columns
    num_rows = df.shape[0]
    num_cols = df.shape[1]

    print("Number of rows: "+str(num_rows))
    print("Number of columns: "+str(num_cols)) 

    

    
    print("\nSorting the success rate of treatment on new TB patients in 2016 in descending order:")
    
    #sort the new TB cases of 2016 in descending order
    selection1 = df.loc[(df["Year"]==2016)].sort_values("Treatment success rate: new TB cases", ascending = False) 
    print(selection1[["Country", "Treatment success rate: new TB cases"]])
    

    #get the average success rate for new TB cases in 2016
    print("The mean success rate in 2016:")
    print(selection1[["Treatment success rate: new TB cases"]].dropna().mean())
    
    #get the median success rate for new TB cases in 2016
    print("The median success rate in 2016:")
    print(selection1[["Treatment success rate: new TB cases"]].dropna().median())
    
    print("\nSorting the success rate of treatment on new TB patients in 1995 in descending order:")
    
    selection2 = df.loc[(df["Year"]==1995)].sort_values("Treatment success rate: new TB cases", ascending = False) 
    print(selection2[["Country", "Treatment success rate: new TB cases"]])
    
    
    #get the average success rate for new TB cases in 1995
    print("The mean success rate in 1995:")
    print(selection2[["Treatment success rate: new TB cases"]].dropna().mean())
    
    #get the median success rate for new TB cases in 1995
    print("The median success rate in 1995:")
    print(selection2[["Treatment success rate: new TB cases"]].dropna().median())
    
    #bottom 10 0f 2016 in new TB
    print("\nThe ten countries with the lowest success rate in treatment of new TB cases in 2016:")
    
    selection3 = df.loc[(df["Year"]==2016)].sort_values("Treatment success rate: new TB cases", ascending = False)
    print(selection3[["Country", "Treatment success rate: new TB cases"]].dropna().tail(10))
    #get the average success rate for bottom 10 new TB cases in 2016
    print("The mean success rate:")
    print(selection3[["Treatment success rate: new TB cases"]].dropna().tail(10).mean())
    
    #get the median success rate for bottom 10 new TB cases in 2016
    print("The median success rate:")
    print(selection3[["Treatment success rate: new TB cases"]].dropna().tail(10).median())
    

    #bottom 10 0f 1995 in new TB
    print("\nThe ten countries with the lowest success rate in treatment of new TB cases in 2016:")
    
    selection4 = df.loc[(df["Year"]==1995)].sort_values("Treatment success rate: new TB cases", ascending = False)
    print(selection4[["Country", "Treatment success rate: new TB cases"]].dropna().tail(10))
    #get the average success rate for bottom 10 new TB cases in 1995
    print("The mean success rate:")
    print(selection4[["Treatment success rate: new TB cases"]].dropna().tail(10).mean())
    
    #get the median success rate for bottom 10 new TB cases in 1995
    print("The median success rate:")
    print(selection4[["Treatment success rate: new TB cases"]].dropna().tail(10).median())
    
    #argentina is the only country in 1995 and 2016 bottom 10- check out its' data, see if it's progressed
    print("\nArgentina's success rate 1995-2016:")
    
    selection5 = df.loc[(df["Country"]=="Argentina")].sort_values("Year", ascending = False)
    print(selection5[["Year", "Treatment success rate: new TB cases"]].dropna())
    #get the average success rate for argentina
    print("The mean success rate:")
    print(selection5[["Treatment success rate: new TB cases"]].dropna().mean())
    
    #get the median success rate for argentina
    print("The median success rate:")
    print(selection5[["Treatment success rate: new TB cases"]].dropna().median())
    
    
pandas1()