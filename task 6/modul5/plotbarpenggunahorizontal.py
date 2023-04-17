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

    bahasa = []
    pengguna = []

    for item in hitung.most_common(15):
        bahasa.append(item[0])
        pengguna.append(item[1])
    
    plt.barh(bahasa,pengguna)

    plt.title("bahasa pemrograman yang paling banyak digunakan")
    plt.xlabel("bahasa pemrograman")
    plt.ylabel("jumlah pengguna")
    plt.show()