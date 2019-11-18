import os
import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(10,5))
plt.subplot(3,2,1)
plt.title("Euler")
data = np.loadtxt('euler.dat')
plt.plot(data[:,0], data[:,1])
plt.xlabel('t')
plt.ylabel('x')

plt.subplot(3,2,2)
plt.title("Rk4")
datos = np.loadtxt('rk4.dat')
plt.plot(datos[:,0], datos[:,1])
plt.xlabel('t')
plt.ylabel('x')

plt.subplot(3,2,3)
plt.title("Euler x vs v")
plt.plot(data[:,1], data[:,2])
plt.xlabel('t')
plt.ylabel('x')

plt.subplot(3,2,4)
plt.title("Rk4")
plt.plot(datos[:,1], datos[:,2])
plt.xlabel('t')
plt.ylabel('x')

plt.savefig('ecuaciones.png')