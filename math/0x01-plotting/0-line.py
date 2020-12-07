#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

y = np.arange(0, 11) ** 3

# create limit axis x
plt.xlim(0, 10)
# create plot

plt.plot(y, color='red')
plt.show()
