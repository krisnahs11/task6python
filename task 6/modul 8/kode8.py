import pandas as pd 
import numpy as np 
from sklearn import linear_model

df = pd.read_csv("datarumah.csv")
reg = linear_model.LinerRegression()
red.fit(df[['luas', 'kamartidur', 'kamarmandi']],df.harga)
