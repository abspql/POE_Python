import pandas as pd 
import numpy as np
 
# Serial
ser = pd.Series() 
print("Pandas Series: ", ser) 


data = np.array(['H', 'e', 'l', 'l', 'o']) 
  
ser = pd.Series(data) 
print("Pandas Series:\n", ser)

#DataFrames

df = pd.DataFrame() 
print(df)

lst = ['Geeks', 'For', 'Geeks', 'is', 'portal', 'for', 'Geeks'] 

df = pd.DataFrame(lst) 
print(df)