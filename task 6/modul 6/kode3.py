import pandas as pd 

pd = pd.read_csv("databand.csv")
nama_band = list(pd['nama band'])
ppb = list(pd['pendengar per bulan'])

print(nama_band)
print(ppb)