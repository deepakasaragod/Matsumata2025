# -*- coding: utf-8 -*-
"""
Example on how to read a .doric file 

"""
# import doric tools to read doric file
import doric as dr #doric tools use numpy and h5py library   
import matplotlib.pyplot as plt
import pandas as pd

if __name__ == "__main__":

    #Set the name of the file that you want to extract the data from in
    #this example the file is in the current folder where we have your python script
    	
    filename = 'F://Matsumata-doric//cCKO63_240708//Console_Acq_0007.doric';
    	    	
    Data_Acquired = dr.ExtractDataAcquisition(filename) #Data_Acquired is a list of dictionary 
    for data in Data_Acquired:
        plt.figure()
        plt.title(data["Name"])
        		
        Signal = data["Data"][0]["Data"]
        Time = data["Data"][1]["Data"][0:len(Signal)]
        plt.plot(Time, Signal)    
    
    isos = Data_Acquired[0]["Data"][1]["Data"]
    photosig = Data_Acquired[1]["Data"][1]["Data"]
    time = Data_Acquired[1]["Data"][0]["Data"]
    dataset = pd.DataFrame({'Time in seconds': time, 'Isos': list(isos), 'Photosig': list(photosig)}, columns=['Time in seconds', 'Isos', 'Photosig'])
    dataset.to_csv(filename.replace('.doric', '.csv'))
