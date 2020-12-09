#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
fruit = np.random.randint(0, 20, (4, 3))

fruit_name = ['apples', 'bananas', 'oranges', 'peaches']
fruit_color = ['red', 'yellow', '#ff8000', '#ffe5b4']
dis_x = np.arange(0, 3)
arr = np.array([0, 0, 0])

for i in range(len(fruit)):
    plt.bar(dis_x, fruit[i], width=0.5, color=fruit_color[i],
            bottom=arr, label=fruit_name[i])
    arr = np.add(arr, fruit[i])

plt.xticks(dis_x, ['Farrah', 'Fred', 'Felicia'])
plt.ylabel("Quantity of Fruit")
plt.yticks(np.arange(0, 90, 10))
plt.title("Number of Fruit per Person")
plt.legend()
plt.show()
