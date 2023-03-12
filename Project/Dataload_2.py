import pandas as pd
import numpy as np


def load_measurements(filename, fmode):
    file = pd.read_csv(filename, header=None).values #open the file (matrix)
    fmode.lower  #makes fmode lower case to prevent errors

    tvec = np.array([])  #create vectors for storing values
    data = np.array([])
    
    neg_line = 0 #initialize the counter of the negative line 

    #print(file)  # print the matrix and some spaces as reference
    #print("\n")


    # 1st check for the case "backward fill" in which the last line has an error
    if fmode == "backward fill" and any(file[len(file)-1][6:] < 0):
        print("Warning, the last line has an error. Mode switched to 'drop'")
        fmode = "drop"  # swithcing mode to "drop"




    for i in range(len(file)):  # loops throught the rows;

        if any(file[i][6:] < 0):  # check every line for an error
            
            # if an error is found the program handeles it according to the given fmode
            
            neg_line += 1 #updates the negative line counter
            
            if fmode == "forward fill":
                if i == 0:  # first line with an error, mode switched to "drop"
                    print("Warning, the first line has an error. Mode switched to 'drop'")
                    fmode = "drop"

                else:
                    tvec = np.append(tvec, file[i][0:6])
                    data = np.append(data, file[i-neg_line][6:]) # otherwise replace the  
                    #line with the latest correct values
    


            elif fmode == "backward fill":
                tvec = np.append(tvec, file[i][0:6])
                errors = 1  #takes note of the number of errors
                for j in range(i+1,len(file)):
                    if any(file[j][6:] < 0):
                        errors += 1 #updates the errors
                    else: 
                        break
                
                data = np.append(data, file[i+errors][6:]) #appends the first good lines without errors


            elif fmode == "drop":
                np.delete(file,[i][:])  # deletes the whole line with the error


        else:  #if there are no errors the matrix is divided into tvec and data
            neg_line = 0 #reset negative line counter
            tvec = np.append(tvec, file[i][0:6])
            data = np.append(data, file[i][6:])

    #creating matrix from the two vectors tvec and data
    tvec = np.reshape(tvec, [int(len(tvec)/6),6])
    data = np.reshape(data, [int(len(data)/4),4])
    print(tvec)
    print(data)
    return tvec, data



load_measurements("2008.csv","backward fill")
