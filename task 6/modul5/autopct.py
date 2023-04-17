from matplotlib import pyplot as plt 

plt.style.use('fivethirtyeight')

slices = [59219, 55466, 47544, 36443, 35917]
label = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']
warna = ['#E5AE37', '#6D904F']
explode = [0, 0, 0, 0.1, 0]

plt.pie(slices, labels=label, explode=explode, shadow=True, startangle=90, autopct='%0.1f%%', wedgeprops={'edgecolor':'black'})

plt.title("contoh pie chart")
plt.tight_layout()
plt.show()