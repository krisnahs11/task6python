import matplotlib.pyplot as plt 

nama_youtuber = ["Mike Denaldi", "Naufal Herma", "Ddims"]
jumlah_subscriber = [25000,5000,30000]

plt.bar(nama_youtuber,jumlah_subscriber)
plt.title("jumlah Subscriber Youtuber")
plt.xlabel("nama youtuber")
plt.ylabel("jumlah subscriber")
plt.show()