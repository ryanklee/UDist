import matplotlib.pyplot as plt
import numpy as np
import time
import pylab as pl
from IPython import display
%matplotlib inline

plt.ion()

while True:
    sampleSize = input("Sample size: ")
    if sampleSize == "q":
        break
    s = np.random.uniform(-1, 1, int(sampleSize))
    count, bins, ignored = plt.hist(s, 15, normed=True)
    print(s)
    plt.plot(bins, np.ones_like(bins), linewidth=1, color='r')
    display.display(plt.gcf())
    display.clear_output(wait=True)
    plt.clf()
    plt.draw()
