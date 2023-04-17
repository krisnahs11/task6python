import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

df = pd.read_csv("datarumah.csv")

from sklearn import linear_model

model_regresi_linear = linear_model.LinearRegression()
plt.xlabel("luas")
plt.ylabel("harga")
plt.scatter(df.luas, df.harga, color='red')
plt.plot(df.luas, model_regresi_linear.predict(df[['luas']]), color='blue')
plt.show()