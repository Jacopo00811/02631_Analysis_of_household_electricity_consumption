import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

def dataPlot(tvec_a, data_a, request):
    data_zones = np.array([])  #array fro the sum of the consumption in each zone 
    axis = np.arange(0,len(tvec_a)) #array for the xaxis
   

    if request.lower() == "all zones":  #check the user's request
        
        for i in range(len(data_a)): #if the user wants all zones the code puts the sum 
            row_value = np.sum(data_a[i,:], axis=0) #of every row in the array data_zones
            data_zones = np.append(data_zones, row_value)
    
         
        if len(data_a) == 24: #check if it is the case of Hour of the day
             plt.bar(axis, data_zones, ec="black") # to plot a more appropriate hist.
             plt.xticks([0, 3, 6, 9, 12, 15, 18, 21, 23],["00:00", " 03:00", "06:00", "09:00", "12:00", "15.00", "18:00", "21:00", "23:00"])
             plt.gca().yaxis.set_major_formatter(mticker.FormatStrFormatter('%d W/h'))
             plt.title("Hour of the day", c="r") #set ticks, titles and the unit of measure
             plt.ylabel("Consumption", c="r")
             plt.xlabel("Hour", c="r")
             plt.show()
             
        elif len(data_a) < 25: #if the rows are less than 25 it plots a bar graph 
             plt.bar(axis, data_zones, ec="black")
             plt.gca().yaxis.set_major_formatter(mticker.FormatStrFormatter('%d W/h'))
             plt.ylabel("Consumption", c="r")
             plt.title("Hist. of data", c="r")
             plt.show()
            
        else: #otherwise it makes a plot
             plt.plot(axis, data_zones, "b.", ls="-", c="b")
             plt.gca().yaxis.set_major_formatter(mticker.FormatStrFormatter('%d W/h'))
             plt.ylabel("Consumption", c="r")
             plt.title("Plot of data", c="r")
             plt.show()
    
             
    else: #now we are in the case where we need to plot alle the zones 
        if len(data_a) == 24: #case of Hour of the day 
            fig_0 = plt.figure(0, figsize=(10, 5)) #creates a figure with a 2x2 grid
               
            chart_1 = fig_0.add_subplot(221) #add the charts to the grid
            chart_2 = fig_0.add_subplot(222)
            chart_3 = fig_0.add_subplot(223)
            chart_4 = fig_0.add_subplot(224)
                 
            chart_1.bar(axis, data_a[:,0], ec="black") #plots the respective column
            chart_2.bar(axis, data_a[:,1], ec="black") #for every zone
            chart_3.bar(axis, data_a[:,2], ec="black")
            chart_4.bar(axis, data_a[:,3], ec="black")
            
            fig_0.suptitle("Hour of the day", c="r", fontsize=15) #set a general title
            
            chart_1.title.set_text("Hist. of zone 1 and 3")#set subtitles
            chart_2.title.set_text("Hist. of zone 2 and 4")

        elif len(data_a) < 25: #if the rows are less than 25 it plots a bar graph 
            fig_1 = plt.figure(1, figsize=(10, 5))
               
            chart_1 = fig_1.add_subplot(221)
            chart_2 = fig_1.add_subplot(222)
            chart_3 = fig_1.add_subplot(223)
            chart_4 = fig_1.add_subplot(224)
                 
            chart_1.bar(axis, data_a[:,0], ec="black")
            chart_2.bar(axis, data_a[:,1], ec="black")
            chart_3.bar(axis, data_a[:,2], ec="black")
            chart_4.bar(axis, data_a[:,3], ec="black")
            
            fig_1.suptitle("Hist. of data", c="r", fontsize=15)
            
            chart_1.title.set_text("Hist. of zone 1 and 3")
            chart_2.title.set_text("Hist. of zone 2 and 4")
 
            plt.show()
       
        else:# otherwise it makes a plot for each zone
            fig_2 = plt.figure(2, figsize=(10, 5))
               
            chart_1 = fig_2.add_subplot(221)
            chart_2 = fig_2.add_subplot(222)
            chart_3 = fig_2.add_subplot(223)
            chart_4 = fig_2.add_subplot(224)
                 
            chart_1.plot(axis, data_a[:,0], "b.", ls="-", c="red")
            chart_2.plot(axis, data_a[:,1], "b.", ls="--", c="blue")
            chart_3.plot(axis, data_a[:,2], "b.", ls=":", c="green")
            chart_4.plot(axis, data_a[:,3], "b.", ls="dotted", c="brown")
                
            fig_2.suptitle("Plot of data", c="r", fontsize=15)
            
            chart_1.title.set_text("Plot of zone 1 and 3")
            chart_2.title.set_text("Plot of zone 2 and 4")

            plt.show()
