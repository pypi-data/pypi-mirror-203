import numpy as np 
import matplotlib.pyplot as plt 

def randhist(n_bins:int, around:int)->None:
    x = np.random.randn(around)
    plt.hist(x, n_bins, histtype='bar', color= "red")
    plt.show()

def randscatter(start_x:int,end_x:int,y:int)->None:
    xData = np.arange(start_x, end_x) 
    yData = xData + 2*np.random.randn(y)
    plt.scatter(xData, yData) 
    plt.show()
