import pandas as pd 
import numpy as np 
from sklearn import linear_model

df = pd.read_csv("datarumah.csv")

import math 
nilai_median_kamartidur = math.floor(df.kamartidur.median())
nilai_median_kamartidur