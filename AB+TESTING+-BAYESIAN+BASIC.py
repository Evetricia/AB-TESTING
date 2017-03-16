
# coding: utf-8

# In[2]:

# From the course: Bayesin Machine Learning in Python: A/B Testing
# https://deeplearningcourses.com/c/bayesian-machine-learning-in-python-ab-testing
# https://www.udemy.com/bayesian-machine-learning-in-python-ab-testing


# In[3]:

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta


# In[4]:

def plot(a, b, trial, ctr):
  x = np.linspace(0, 1, 200)
  y = beta.pdf(x, a, b)
  mean = float(a) / (a + b)
  plt.plot(x, y)
  plt.title("Distributions after %s trials, true rate = %.1f, mean = %.2f" % (trial, ctr, mean))
  plt.show()


# In[10]:

true_ctr = 0.3
a, b = 1, 1 # beta parameters


# In[11]:

show = [0, 5, 10, 25, 50, 100, 200, 300, 500, 700, 1000, 1500]


# In[14]:

for t in range(1501):
  coin_toss_result = (np.random.random() < true_ctr)
  if coin_toss_result:
    a += 1
  else:
    b += 1

  if t in show:
    plot(a, b, t+1, true_ctr)

