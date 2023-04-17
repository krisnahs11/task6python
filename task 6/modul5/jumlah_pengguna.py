from matplotlib import pyplot as plt 
import numpy as np 
import csv 
from collections import Counter

plt.style.use('fivethirtyeight')

with open('penggunabahasapemrograman.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    hitung= Counter()

    for row in csv_reader:
        hitung.update(row['jumlah pengguna'].split(';'))
    print(hitung)