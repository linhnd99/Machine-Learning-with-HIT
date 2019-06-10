import pandas as pd  
import numpy as np 
from ex1 import *

def convertScreenSize(sc):
    sc=sc.strip()
    sc = sc[:-1]
    sc.replace(",",".")
    return float(sc)

def PopularScreenSize():
    print(laptops.screen_size.value_counts())

def MinScreenSizeOfUltrabook():
    test = laptops.loc[laptops.category == "Ultrabook",:]
    print("Minimum Screen Size Of Ultrabook : %f " % test.screen_size.min())

def AverageScreenSizeGamingLaptop():
    arr_filter = laptops.loc[laptops.category == "Gaming",:]
    average = arr_filter.screen_size.sum()/len(arr_filter.screen_size)
    return average
    
if __name__=="__main__":
    laptops.screen_size = [convertScreenSize(el) for el in laptops.screen_size]
    PopularScreenSize()
    MinScreenSizeOfUltrabook()
    print(AverageScreenSizeGamingLaptop())