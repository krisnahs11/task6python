from matplotlib import pyplot as plt 

plt.style.use('fivethirtyeight')

slices = [60, 40]
label = ['60', '40']

plt.pie(slices, labels=label, )

plt.title("contoh pie chart labels")
plt.tight_layout()
plt.show()