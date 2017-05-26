import numpy as np
import matplotlib.pyplot as plt

#Se cargan y se guardan todos los datos obtenidos en el archivo canal_ionico.c
data = np.loadtxt('Canal_ionico.txt')
data1 = np.loadtxt('Canal_ionico1.txt')
data2 = np.loadtxt('resultados1.txt')
data3 = np.loadtxt('resultados2.txt')
data4 = np.loadtxt('1rta.txt')
data5 = np.loadtxt('2rta.txt')

x = data[:,0]
y = data[:,1]
x1 = data1[:,0]
y1 = data1[:,1]
x2 = data2[:,0]
y2 = data2[:,1]
z2 = data2[:,2]
x3 = data3[:,0]
y3 = data3[:,1]
z3 = data3[:,2]
x4 = data4[:,0]
y4 = data4[:,1]
x5 = data5[:,0]
y5 = data5[:,1]
            
#Gráfica Canal_ionico.txt
fig = plt.gcf()
ax = fig.gca()

#Se usaron los datos arrojados en la consola, al momento de compilar por última vez, x = 3.433143, y = 5.483226, r = 6.423794
plt.scatter(x,y, color='b')
plt.scatter(3.433143,5.483226)
plt.xlabel('Angstrom(Å)')
plt.ylabel('Angstrom(Å)')
plt.title('Canal Iónico (x = 3.433143Å, y = 5.483226Å, r = 6.423794Å)')

cir= plt.Circle((3.433143, 5.483226), 6.423794, color='r', fill=False)
ax.add_artist(cir)
plt.savefig('GraficaCanal_Ionico.png')


#Gráfica Canal_ionico1.txt
fig2 = plt.gcf()
ax2 = fig2.gca()
#Se usaron los datos arrojados en la consola, al momento de compilar por última vez x = 3.331520, y= 3.848832, r = 5.780902

plt.scatter(x1,y1, color='b')
plt.scatter(3.331520,3.848832)
plt.xlabel('Angstrom(Å)')
plt.ylabel('Angstrom(Å)')
plt.title('Canal Iónico1 (x = 3.331520Å, y= 3.848832Å, r = 5.780902Å)')

cir2= plt.Circle((3.331520, 3.848832), 5.780902, color='r', fill=False)
ax2.add_artist(cir2)
plt.savefig('GraficaCanal_Ionico1.png')

#Histogramas valores x, y del centro del círculo primer archivo
plt.figure()
plt.subplot(2, 1, 1)
count, bins, ignored = plt.hist(x2, 50, normed=True) 
plt.title('Histogramas Resultados1')
plt.ylabel('Angstrom(Å)')
plt.xlim(2,5)
plt.subplot(2, 1, 2)
count, bins, ignored = plt.hist(y2, 50, normed=False)
plt.xlabel('Angstrom(Å)')
plt.ylabel('Angstrom(Å)')
plt.xlim(4,7)
plt.savefig('HistogramasCanalIonico.png')

#Histogramas valores x, y del centro del círculo segundo archivo
plt.figure()
plt.subplot(2, 1, 1)
count, bins, ignored = plt.hist(x3, 50, normed=True) 
plt.title('Histogramas Resultados2')
plt.ylabel('Angstrom(Å)')
plt.xlim(2,5)
plt.subplot(2, 1, 2)
count, bins, ignored = plt.hist(y3, 50, normed=False)
plt.xlabel('Angstrom(Å)')
plt.ylabel('Angstrom(Å)')
plt.xlim(2,5)
plt.savefig('HistogramasCanalIonico1.png')



