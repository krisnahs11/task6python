import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 

df = pd.read_csv("datarumah.csv")

from sklearn import linear_model

model_regresi_linear = linear_model.LinearRegression()
model_regresi_linear.intercef_