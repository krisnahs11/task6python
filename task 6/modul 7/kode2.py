import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

df = pd.read_csv("datarumah.csv")
plt.xlabel("luas")
plt.ylabel("harga")
plt.scatter(df.luas, df.harga, color='red')
plt.show()