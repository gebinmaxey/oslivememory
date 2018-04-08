import numpy as np
import matplotlib.pyplot as plt
from psutil import virtual_memory

explode = (0,0.1)

fig1, ax1 = plt.subplots()
labels = 'Used','Free'
plt.title('Ram Usage')
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

while 10 < 12:
    mem = virtual_memory()
    sizes = [mem.used, mem.available]
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)

    plt.pause(0.05)
    plt.draw()
