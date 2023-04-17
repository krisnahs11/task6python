from matplotlib import pyplot as plt 

plt.style.use('fivethirtyeight')

slices = [60, 40]
label = ['60', '40']



plt.pie(slices, labels=label, wedgeprops={'edgecolor':'black'})

plt.title("contoh pie chart wedgeprops")
plt.tight_layout()
plt.show()