import matplotlib.pyplot as plt
import psutil

mem = psutil.disk_usage('/')

labels = 'Used','Free'

sizes = [mem.used, mem.free]

explode = (0,0.1)

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)

ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.title('Disk Usage')
plt.show()
