import numpy as np
from tabulate import tabulate as tb
from Dataload_2 import load_measurements

tvec, data = load_measurements("testdata1.csv","backward fill")


def print_statistics(tvec, data):
    
    #print(data)
    #finds the minimum using the numpy function 
    min_1 = np.amin(data[:,0])
    min_2 = np.amin(data[:,1])
    min_3 = np.amin(data[:,2])
    min_4 = np.amin(data[:,3])
    Min = np.amin(data)
    #finds the maximum using the numopy function 
    max_1 = np.amax(data[:,0])
    max_2 = np.amax(data[:,1])
    max_3 = np.amax(data[:,2])
    max_4 = np.amax(data[:,3])
    Max = np.amax(data)
    #finds the second quartile (aka median) using the numpy function 
    second_Quart_1 = np.median(data[:,0])
    second_Quart_2 = np.median(data[:,1])
    second_Quart_3 = np.median(data[:,2])
    second_Quart_4 = np.median(data[:,3])
    second_Quart = np.median(data)
    #finds the first quartile using the nummpy function
    first_Quart_1 = np.percentile(data[:,0], 25)
    first_Quart_2 = np.percentile(data[:,1], 25)
    first_Quart_3 = np.percentile(data[:,2], 25)
    first_Quart_4 = np.percentile(data[:,3], 25)
    first_Quart = np.percentile(data, 25)
    #finds the third quartile using the numpy function 
    third_Quart_1 = np.percentile(data[:,0], 75)
    third_Quart_2 = np.percentile(data[:,1], 75)
    third_Quart_3 = np.percentile(data[:,2], 75)
    third_Quart_4 = np.percentile(data[:,3], 75)
    third_Quart = np.percentile(data, 75) 
    
    #storing the values in a matrix called table according to  the order I want to diplay them 
    table = np.array([['Zone','Minimum','1 Quart.','2 Quart.','3 Quart.','Maximum'],
                     [1, min_1 , first_Quart_1, second_Quart_1, third_Quart_1, max_1],
                     [2, min_2, first_Quart_2, second_Quart_2, third_Quart_2, max_2],
                     [3, min_3, first_Quart_3, second_Quart_3, third_Quart_3, max_3],
                     [4, min_4, first_Quart_4, second_Quart_4, third_Quart_4, max_4],
                     ['All', Min, first_Quart, second_Quart, third_Quart, Max]])
    #show the table 
    print(tb(table, headers='firstrow', tablefmt='fancy_grid'))
    
    return



print_statistics(tvec, data)