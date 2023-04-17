from matplotlib import pyplot as plt 

plt.style.use('fivethirtyeight')

slices = [60, 40]

plt.pie(slices )

plt.title("contoh pie chart slices")
plt.tight_layout()
plt.show()