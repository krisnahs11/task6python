%matplotlib notebook

from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

hari =[4,6,10,13,16,20,22,24,26,28,30]
young_lex = [100,120,160,180,210,240,270,320,330,350]
plt.bar(hari,young_lex,color='#444444', label='young lex')

atta = (120,140,200,230,260,280,290,320,330,380,400)
plt.plot(hari,atta, color='#5A7D9A', label='atta halilintar')

plt.title('kenaikan subscriber berdasarkan hari')
plt.xlabel('hari')
plt.ylabel('jumlah subscirber')

plt.legend(['young lex', 'atta halilintar'])
plt.grid(True)
plt.tight_layout()
plt.show()