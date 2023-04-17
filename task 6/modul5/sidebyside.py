%matplotlib notebook

from matplotlib import pyplot as plt
import numpy as np 

plt.style.use('fivethirtyeight')

hari =[4,6,10,13,16,20,22,24,26,28,30]

x_indeks= np.arange(len(hari))

lebar_bar = 0.35
print(len(hari))
print(x_indeks)
print(x_indeks-lebar_bar)

atta = (120,140,200,230,260,280,290,320,330,380,400)
plt.bar(hari,atta, width=lebar_bar, color='#008FD5', label='atta halilintar')

young_lex = [100,120,160,180,210,240,270,320,330,350]
plt.bar(hari,young_lex, width=lebar_bar, color='#E5AE38', label='young lex')


plt.title('kenaikan subscriber berdasarkan hari')
plt.xlabel('hari')
plt.ylabel('jumlah subscirber')

plt.xticks(ticks=x_indeks, labels=hari)

plt.legend(['young lex', 'atta halilintar'])
plt.grid(True)
plt.tight_layout()
plt.show()