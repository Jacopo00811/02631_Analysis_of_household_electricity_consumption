# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 11:40:18 2021

@author: user
"""

import pandas as pd
import numpy as np
from Dataload_2 import load_measurements



tvec, data = load_measurements("testdata1.csv","backward fill")
period = "day"


def aggregate_measurments(tvec,data,period):
    
    # we join the two data frames so we can group everything more easily
    frames = [tvec, data]
    file = pd.concat(frames)
    # we name the time vectors and the data recorded corresponding with the zones
    file.columns = ['Year', 'Month','Day', 'Hour','Minute','Second','zone1','zone2', 'zone3', 'zone4']
    
    if period == 'hour':
        # to sum the data collected in the same hour
        hr = file.groupby('Hour')[['zone1','zone2', 'zone3', 'zone4']].sum()
        # to separate the values of hours in tvec_a and the aggregated data in data_a
        tvec_a = list(hr.index)
        data_a = hr.values
        
    if period == 'day':
        # to sum the data collected in the same day
        dy = file.groupby('Day')[['zone1','zone2', 'zone3', 'zone4']].sum()
        tvec_a = list(dy.index)
        data_a = dy.values
        
    if period == 'month':
        # to sum the data collected in the same month
        mh = file.groupby('Month')[['zone1','zone2', 'zone3', 'zone4']].sum()
        tvec_a = list(mh.index)
        data_a = mh.values
        
    if period == 'hour of the day':
        # first we create an empty data frame with the required 24 hours per day
        df = pd.DataFrame(np.zeros((24,0)))
        # we sum the data collected in the same hour of the day
        df1 = file.groupby('Hour')[['zone1','zone2', 'zone3', 'zone4']].sum()
        # we join the two data frames and fill the NaN spaces with zeros, as we have no data recorded in that time
        hrd = df.join(df1).fillna(0)    
        tvec_a = list(hrd.index)
        data_a = hrd.values  


     
    
    
    return(tvec_a, data_a)


print(aggregate_measurments(tvec,data,period))


















