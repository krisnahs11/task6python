# %matplotlib notebook untuk melakukan zoom in,out,move (berinteraksi dengan plot)
%matplotlib notebook

from matplotlib import pyplot as plt

sumbux = [4,6,10,13,16,20,22,24,26,28,30]
sumbuy = [100,120,160,180,210,240,270,320,330,350]
plt.plot(sumbux,sumbuy)

plt.title('kenaikan subscriber berdasarkan hari')
plt.xlabel('hari')
plt.ylabel('jumlah subscriber')
plt.show()