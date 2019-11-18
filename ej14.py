import os
import numpy as np
import matplotlib.pyplot as plt

plt.figure()
data = np.loadtxt('ej14.dat')
plt.plot(data[:,0], data[:,1])
plt.xlabel('t')
plt.ylabel('x')
plt.savefig('euler.png')