import pandas as pd 
import numpy as np 
from sklearn import linear_model

df = pd.read_csv("datarumah.csv")
df.replace(0, np.nan, inplace=true)
df