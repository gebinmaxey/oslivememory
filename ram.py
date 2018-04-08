import matplotlib.pyplot as plt
from psutil import virtual_memory

mem = virtual_memory()

labels = 'Used','Free'

sizes = [mem.used, mem.available]

explode = (0,0.1)

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)

ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.title('Ram Usage')
plt.draw()
