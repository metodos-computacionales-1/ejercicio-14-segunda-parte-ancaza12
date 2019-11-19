import os
import numpy as np
import matplotlib.pyplot as plt

plt.figure(figsize=(10,7))

plt.subplot(3,3,1)
plt.title("Euler: t vs y[0]")
data = np.loadtxt('euler.dat')
plt.plot(data[:,0], data[:,1])
plt.xlabel('t')
plt.ylabel('y[0]')

plt.subplot(3,3,2)
plt.title("Euler: t vs y[1]")
data = np.loadtxt('euler.dat')
plt.plot(data[:,0], data[:,2])
plt.xlabel('t')
plt.ylabel('y[1]')

plt.subplot(3,3,3)
plt.title("Euler: y[0] vs y[1]")
plt.plot(data[:,1], data[:,2])
plt.xlabel('y[0]')
plt.ylabel('y[1]')

plt.subplot(3,3,4)
plt.title("Rk4: t vs y[0]")
datos = np.loadtxt('rk4.dat')
plt.plot(datos[:,0], datos[:,1])
plt.xlabel('t')
plt.ylabel('y[0]')

plt.subplot(3,3,5)
plt.title("Rk4: t vs y[1]")
datos = np.loadtxt('rk4.dat')
plt.plot(datos[:,0], datos[:,2])
plt.xlabel('t')
plt.ylabel('y[1]')

plt.subplot(3,3,6)
plt.title("Rk4: y[0] vs y[1]")
plt.plot(datos[:,1], datos[:,2])
plt.xlabel('y[0]')
plt.ylabel('y[1]')

plt.subplot(3,3,7)
dat = np.loadtxt('fric.dat')
plt.title("Friccion: t vs y[0]")
plt.plot(dat[:,0], dat[:,1])
plt.xlabel('t')
plt.ylabel('y[0]')

plt.subplot(3,3,8)
dat = np.loadtxt('fric.dat')
plt.title("Friccion: t vs y[1]")
plt.plot(dat[:,0], dat[:,2])
plt.xlabel('t')
plt.ylabel('y[1]')

plt.subplot(3,3,9)
dat = np.loadtxt('fric.dat')
plt.title("Friccion: y[0] vs y[1]")
plt.plot(dat[:,1], dat[:,2])
plt.xlabel('y[0]')
plt.ylabel('y[1]')

plt.subplots_adjust(wspace=0.3, hspace=0.8)
plt.savefig('ecuaciones.png')