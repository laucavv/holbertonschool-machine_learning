#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
student_grades = np.random.normal(68, 15, 50)
# labels
plt.xlabel('Grades')
plt.ylabel('Number of Students')
plt.title('Project A')
# limits
plt.xlim(0)
plt.ylim([0, 30])
plt.xticks(np.arange(0, 101, step=10))
# create graph
plt.hist(student_grades, edgecolor='black')
plt.show()
