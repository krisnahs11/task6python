import pandas  as pd 

sample = pd.read_csv("sampledataok.csv")

filter1= sample['umur']>28
filterbaru = sample[filter1]
filterbaru