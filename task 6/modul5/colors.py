from matplotlib import pyplot as plt 

plt.style.use('fivethirtyeight')

slices = [60, 40]
label = ['60', '40']
warna = ['#E5AE37', '#6D904F']


plt.pie(slices, labels=label, colors=warna, wedgeprops={'edgecolor':'black'})

plt.title("contoh pie chart colors")
plt.tight_layout()
plt.show()