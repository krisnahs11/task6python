import pandas as pd 
import numpy as np 
from sklearn import linear_model

df = pd.read_csv("datarumah.csv")
df.at[2, 'kamar tidur']=0
df