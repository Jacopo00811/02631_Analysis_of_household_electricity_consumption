import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from Dataload_2 import load_measurements
from matplotlib.ticker import MaxNLocator

"""x = 0 will be the user choice in the main script 
if x == "Visualize electricity consumption." or x == 4:
request = input("Do you want to plot the consumption in each zone or the combined consumption (all zones)?")
   dataPlot(tvec_a, data_a, request)"""




period = "hour"
request = "all zones"
tvec_a, data_a = load_measurements("try_2.csv","backward fill")


data_zones = np.array([])   
def dataPlot(tvec_a, data_a, request):
    data_zones = np.array([])  #try if it resets
    
    
    if request.lower == "all zones":
        
        for i in range(len(data_a)):
            row_value = np.sum(data_a[i], axis=0)
            data_zones = np.append(data_zones, row_value)
        
        if len(data_a) < 25:
            if period == "minute":
                #get the 5th column of the tvec_a matrix
                plt.hist(tvec_a[:,4], data_zones, ec="black")
                plt.xaxis.set_major_locator(MaxNLocator(integer=True))  
                plt.show()
                
            elif period == "hour":
                #get the 4th column of the tvec_a matrix
                plt.hist(tvec_a[:,3], data_zones, ec="black")
                plt.xaxis.set_major_locator(MaxNLocator(integer=True))
                plt.show()
                
            elif period == "day":
                #get the 3rd column of the tvec_a matrix
                plt.hist(tvec_a[:,2], data_zones, ec="black")
                plt.xaxis.set_major_locator(MaxNLocator(integer=True))
                plt.show()
                
            elif period == "month":
                #get the 2nd column of the tvec_a matrix
                plt.hist(tvec_a[:,1], data_zones, ec="black")
                plt.xaxis.set_major_locator(MaxNLocator(integer=True))
                plt.show()
                
            else:
                #case of hour of the day
                plt.hist(tvec_a[:,3], data_zones, ec="black") 
                plt.xaxis.set_major_locator(MaxNLocator(integer=True))
                plt.show()
                
        else:
            if period == "minute":
                #get the 4th column of the tvec_a matrix
                plt.plot(tvec_a[:,4], data_zones, "b.", ls="-", c="red")
                plt.xaxis.set_major_locator(MaxNLocator(integer=True))
                plt.show()
                
            elif period == "hour":
                #get the 4th column of the tvec_a matrix
                plt.plot(tvec_a[:,3], data_zones, "b.", ls="-", c="red")
                plt.xaxis.set_major_locator(MaxNLocator(integer=True))
                plt.show()
                
            elif period == "day":
                #get the 3rd column of the tvec_a matrix
                plt.plot(tvec_a[:,2], data_zones, "b.", ls="--", c="blue")
                plt.xaxis.set_major_locator(MaxNLocator(integer=True))
                plt.show()
                
            elif period == "month":
                #get the 2nd column of the tvec_a matrix
                plt.plot(tvec_a[:,1], data_zones, "b.", ls=":", c="green")
                plt.xaxis.set_major_locator(MaxNLocator(integer=True))
                plt.show()
                
            
            
    else:
       if len(data_a) < 25:
           if period == "minute":
               fig_0 = plt.figure(0, figsize=(20, 4.8))
               
               chart_1 = fig_0.add_subplot(221)
               chart_2 = fig_0.add_subplot(222)
               chart_3 = fig_0.add_subplot(223)
               chart_4 = fig_0.add_subplot(224)
                 
               chart_1.hist(tvec_a[:,4], data_a[:,0], ec="black")
               chart_2.hist(tvec_a[:,4], data_a[:,1], ec="black")
               chart_3.hist(tvec_a[:,4], data_a[:,2], ec="black")
               chart_4.hist(tvec_a[:,4], data_a[:,3], ec="black")
                
               chart_1.xaxis.set_major_locator(MaxNLocator(integer=True))
               chart_2.xaxis.set_major_locator(MaxNLocator(integer=True))
               chart_3.xaxis.set_major_locator(MaxNLocator(integer=True))
               chart_4.xaxis.set_major_locator(MaxNLocator(integer=True))
               plt.show()
               
           elif period == "hour":
               fig_1 = plt.figure(1, figsize=(20, 4.8))
               
               chart_1 = fig_1.add_subplot(221)
               chart_2 = fig_1.add_subplot(222)
               chart_3 = fig_1.add_subplot(223)
               chart_4 = fig_1.add_subplot(224)
               
               chart_1.hist(tvec_a[:,3], data_a[:,0], ec="black")
               chart_2.hist(tvec_a[:,3], data_a[:,1], ec="black")
               chart_3.hist(tvec_a[:,3], data_a[:,2], ec="black")
               chart_4.hist(tvec_a[:,3], data_a[:,3], ec="black")
                
               chart_1.xaxis.set_major_locator(MaxNLocator(integer=True))
               chart_2.xaxis.set_major_locator(MaxNLocator(integer=True))
               chart_3.xaxis.set_major_locator(MaxNLocator(integer=True))
               chart_4.xaxis.set_major_locator(MaxNLocator(integer=True))
               plt.show()
               
           elif period == "day":
               fig_2 = plt.figure(2, figsize=(20, 4.8))
                
               chart_1 = fig_2.add_subplot(221)
               chart_2 = fig_2.add_subplot(222)
               chart_3 = fig_2.add_subplot(223)
               chart_4 = fig_2.add_subplot(224)
            
               chart_1.hist(tvec_a[:,2], data_a[:,0], ec="black")
               chart_2.hist(tvec_a[:,2], data_a[:,1], ec="black")
               chart_3.hist(tvec_a[:,2], data_a[:,2], ec="black")
               chart_4.hist(tvec_a[:,2], data_a[:,3], ec="black")
        
               chart_1.xaxis.set_major_locator(MaxNLocator(integer=True))
               chart_2.xaxis.set_major_locator(MaxNLocator(integer=True))
               chart_3.xaxis.set_major_locator(MaxNLocator(integer=True))
               chart_4.xaxis.set_major_locator(MaxNLocator(integer=True))
               plt.show()
               
           elif period == "month":
               fig_3 = plt.figure(3, figsize=(20, 4.8))
               
               chart_1 = fig_3.add_subplot(221)
               chart_2 = fig_3.add_subplot(222)
               chart_3 = fig_3.add_subplot(223)
               chart_4 = fig_3.add_subplot(224)
            
               chart_1.hist(tvec_a[:,1], data_a[:,0], ec="black")
               chart_2.hist(tvec_a[:,1], data_a[:,1], ec="black")
               chart_3.hist(tvec_a[:,1], data_a[:,2], ec="black")
               chart_4.hist(tvec_a[:,1], data_a[:,3], ec="black")
                
               chart_1.xaxis.set_major_locator(MaxNLocator(integer=True))
               chart_2.xaxis.set_major_locator(MaxNLocator(integer=True))
               chart_3.xaxis.set_major_locator(MaxNLocator(integer=True))
               chart_4.xaxis.set_major_locator(MaxNLocator(integer=True))
               plt.show()
               
           else:#hour of the day
               fig_4 = plt.figure(4, figsize=(20, 4.8))
               
               chart_1 = fig_4.add_subplot(221)
               chart_2 = fig_4.add_subplot(222)
               chart_3 = fig_4.add_subplot(223)
               chart_4 = fig_4.add_subplot(224)
                 
               chart_1.hist(tvec_a[:,3], data_a[:,0], ec="black")
               chart_2.hist(tvec_a[:,3], data_a[:,1], ec="black")
               chart_3.hist(tvec_a[:,3], data_a[:,2], ec="black")
               chart_4.hist(tvec_a[:,3], data_a[:,3], ec="black")
                
               chart_1.xaxis.set_major_locator(MaxNLocator(integer=True))
               chart_2.xaxis.set_major_locator(MaxNLocator(integer=True))
               chart_3.xaxis.set_major_locator(MaxNLocator(integer=True))
               chart_4.xaxis.set_major_locator(MaxNLocator(integer=True))
               plt.show()
               
       else:
           if period == "minute":
               fig_5 = plt.figure(5, figsize=(20, 4.8))
               
               chart_1 = fig_5.add_subplot(221)
               chart_2 = fig_5.add_subplot(222)
               chart_3 = fig_5.add_subplot(223)
               chart_4 = fig_5.add_subplot(224)
                 
               chart_1.plot(tvec_a[:,4], data_a[:,0], "b.", ls="-", c="red")
               chart_2.plot(tvec_a[:,4], data_a[:,1], "b.", ls="--", c="blue")
               chart_3.plot(tvec_a[:,4], data_a[:,2], "b.", ls=":", c="green")
               chart_4.plot(tvec_a[:,4], data_a[:,3], "b.", ls="dotted", c="brown")
                
               chart_1.xaxis.set_major_locator(MaxNLocator(integer=True))
               chart_2.xaxis.set_major_locator(MaxNLocator(integer=True))
               chart_3.xaxis.set_major_locator(MaxNLocator(integer=True))
               chart_4.xaxis.set_major_locator(MaxNLocator(integer=True))
               plt.show()
               
           elif period == "hour":
               fig_6 = plt.figure(6, figsize=(40, 15))
               
               
               x = np.arange(0,len(tvec_a))
               
               
               chart_1 = fig_6.add_subplot(221)
               chart_2 = fig_6.add_subplot(222)
               chart_3 = fig_6.add_subplot(223)
               chart_4 = fig_6.add_subplot(224)
                 
               chart_1.plot(x, data_a[:,0], "b.", ls="-", c="red")
               chart_2.plot(x, data_a[:,1], "b.", ls="--", c="blue")
               chart_3.plot(x, data_a[:,2], "b.", ls=":", c="green")
               chart_4.plot(x, data_a[:,3], "b.", ls="dotted", c="brown")
                
               chart_1.xaxis.set_major_locator(MaxNLocator(integer=True))
               chart_2.xaxis.set_major_locator(MaxNLocator(integer=True))
               chart_3.xaxis.set_major_locator(MaxNLocator(integer=True))
               chart_4.xaxis.set_major_locator(MaxNLocator(integer=True))
               plt.show()
               
           elif period == "day":
               fig_7 = plt.figure(7, figsize=(40, 15))
        
               chart_1 = fig_7.add_subplot(221)
               chart_2 = fig_7.add_subplot(222)
               chart_3 = fig_7.add_subplot(223)
               chart_4 = fig_7.add_subplot(224)
                 
               chart_1.plot(tvec_a[:,2], data_a[:,0], "b.", ls="-", c="red")
               chart_2.plot(tvec_a[:,2], data_a[:,1], "b.", ls="--", c="blue")
               chart_3.plot(tvec_a[:,2], data_a[:,2], "b.", ls=":", c="green")
               chart_4.plot(tvec_a[:,2], data_a[:,3], "b.", ls="dotted", c="brown")
                
               chart_1.xaxis.set_major_locator(MaxNLocator(integer=True))
               chart_2.xaxis.set_major_locator(MaxNLocator(integer=True))
               chart_3.xaxis.set_major_locator(MaxNLocator(integer=True))
               chart_4.xaxis.set_major_locator(MaxNLocator(integer=True))
               plt.show()
               
           elif period == "month":
               fig_8 = plt.figure(8, figsize=(20, 4.8))
               
               chart_1 = fig_8.add_subplot(221)
               chart_2 = fig_8.add_subplot(222)
               chart_3 = fig_8.add_subplot(223)
               chart_4 = fig_8.add_subplot(224)
                 
               chart_1.plot(tvec_a[:,1], data_a[:,0], "b.", ls="-", c="red")
               chart_2.plot(tvec_a[:,1], data_a[:,1], "b.", ls="--", c="blue")
               chart_3.plot(tvec_a[:,1], data_a[:,2], "b.", ls=":", c="green")
               chart_4.plot(tvec_a[:,1], data_a[:,3], "b.", ls="dotted", c="brown")
                
               chart_1.xaxis.set_major_locator(MaxNLocator(integer=True))
               chart_2.xaxis.set_major_locator(MaxNLocator(integer=True))
               chart_3.xaxis.set_major_locator(MaxNLocator(integer=True))
               chart_4.xaxis.set_major_locator(MaxNLocator(integer=True))
               plt.show()
               
dataPlot(tvec_a, data_a, request)