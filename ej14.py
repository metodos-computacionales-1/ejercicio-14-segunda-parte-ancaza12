import os
import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(10,5))
plt.subplot(2,3,1)
plt.title("Euler")
data = np.loadtxt('ej14.dat')
plt.plot(data[:,0], data[:,1])
plt.xlabel('t')
plt.ylabel('x')

plt.subplot(2,3,2)
plt.title("Rk4")

datos = np.loadtxt('datosrk4.dat')
plt.plot(data[:,0], data[:,1])
plt.xlabel('t')
plt.ylabel('x')
plt.savefig('ecuaciones.png')