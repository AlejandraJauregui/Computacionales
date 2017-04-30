import numpy as np
import matplotlib.pyplot as plt 

#Se descargan los archivos de texto que C arrojaría

datos = np.loadtxt('t1.txt')  
datoss = np.loadtxt('t2.txt')
datosss = np.loadtxt('t3.txt')

#Gráfica 1
Graf1 = plt.figure(1)(figsize =(15,15))
plt.imshow(datos)
plt.grid(True)
plt.savefig("Gráfica1.png")              

#Gráfica 2
Graf2= plt.figure(2)
plt.imshow(datoss)
plt.grid(True)
plt.savefig("Gráfica2.png")


#Gráfica 3
Graf3 = plt.figure(3)
plt.imshow(datosss)
plt.grid(True)
plt.savefig("Gráfica3.png")


