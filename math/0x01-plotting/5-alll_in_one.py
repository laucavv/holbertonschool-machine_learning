#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

y0 = np.arange(0, 11) ** 3

mean = [69, 0]
cov = [[15, 8], [8, 15]]
np.random.seed(5)
x1, y1 = np.random.multivariate_normal(mean, cov, 2000).T
y1 += 180

x2 = np.arange(0, 28651, 5730)
r2 = np.log(0.5)
t2 = 5730
y2 = np.exp((r2 / t2) * x2)

x3 = np.arange(0, 21000, 1000)
r3 = np.log(0.5)
t31 = 5730
t32 = 1600
y31 = np.exp((r3 / t31) * x3)
y32 = np.exp((r3 / t32) * x3)

np.random.seed(5)
student_grades = np.random.normal(68, 15, 50)

# create  figure

fig = plt.figure()
fig.suptitle('All in One')

grid = fig.add_gridspec(3, 2)

graph_1 = fig.add_subplot(grid[0, 0])
graph_2 = fig.add_subplot(grid[0, 1])
graph_3 = fig.add_subplot(grid[1, 0])
graph_4 = fig.add_subplot(grid[1, 1])
graph_5 = fig.add_subplot(grid[2, :])
fig.tight_layout(pad=2.5)
# create graph 1
graph_1.set_xlim(0, 10)
graph_1.plot(y0, color='red')

# create graph2
graph_2.set_ylabel('Weight (lbs)', fontsize='x-small')
graph_2.set_xlabel('Height (in)', fontsize='x-small')
graph_2.set_title('Men\'s Height vs Weight', fontsize='x-small')
graph_2.scatter(x1, y1, s=10, color='magenta')

# create graph3

graph_3.set_xlabel('Time (years)', fontsize='x-small')
graph_3.set_ylabel('Fraction Remaining', fontsize='x-small')
graph_3.set_title('Exponential Decay of C-14', fontsize='x-small')

graph_3.set_xlim(0, 28650)
graph_3.set_yscale('log')
graph_3.plot(x2, y2)

# create graph4
graph_4.set_xlabel('Time (years)', fontsize='x-small')
graph_4.set_ylabel('Fraction Remaining', fontsize='x-small')
graph_4.set_title('Exponential Decay of Radioactive Elements',
                  fontsize='x-small')
graph_4.set_xlim([0, 20000])
graph_4.set_ylim([0, 1])

graph_4.plot(x3, y31, color='red', linestyle='dashed', label='C-14')
graph_4.plot(x3, y32, color='green', label='Ra-226')
graph_4.legend(fontsize='x-small')


# create graph5

graph_5.set_xlabel('Grades', fontsize='x-small')
graph_5.set_ylabel('Number of Students', fontsize='x-small')
graph_5.set_title('Project A', fontsize='x-small')
# limits
graph_5.set_xlim(0)
graph_5.set_ylim([0, 30])
graph_5.set_xticks(np.arange(0, 101, step=10))

graph_5.hist(student_grades, edgecolor='black')
plt.show()
