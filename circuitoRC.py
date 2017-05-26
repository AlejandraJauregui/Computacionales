import numpy as np
import matplotlib.pyplot as plt 
from scipy.interpolate import griddata

#Lee el archivo 
datos = np.loadtxt('CircuitoRC.txt')

t = datos[:,0]
y = datos[:,1]

#Usar un metodo de determinacion bayesiana de parámetros con Monte Carlo para obtener R y C a partir de los datos experimentales.

def likelihood(y, y2):
    chi = (1.0/2.0)*np.sum(((y-y2)/1000)**2)
    
    return np.exp(-chi)

#miu = 1/RC
#Q = Vo*C

def my_model(t, Q, miu):
    return Q*(1-np.exp(-t*miu))

Q_walk = [] 
miu_walk = []
l_walk = []

Q_walk = np.append(Q_walk, np.random.random())
miu_walk = np.append(miu_walk, np.random.random())

yini = my_model(t, Q_walk[0], miu_walk[0])
l_walk = np.append(l_walk, likelihood(y, yini))

#print(Q_walk)
#print(miu_walk)
#print(l_walk)


n = 7000 #this is the number of iterations I want to make
for i in range(0,n):
    
    Q_prime = np.random.normal(Q_walk[i], 100) 
    miu_prime = np.random.normal(miu_walk[i],0.1)

    yini = my_model(t, Q_walk[i], miu_walk[i])
    y_prime = my_model(t, Q_prime, miu_prime)
    
    l_prime = likelihood(y, y_prime)
    l_init = likelihood(y, yini)
    
    #print(l_init)
    #print(l_prime)
    
    alpha = l_prime/l_init
    if(alpha>=1.0):
        Q_walk  = np.append(Q_walk,Q_prime)
        miu_walk  = np.append(miu_walk,miu_prime)
        l_walk = np.append(l_walk, l_prime)
        
    else:
        
        beta = np.random.random()
        if(beta<=alpha):
            Q_walk = np.append(Q_walk,Q_prime)
            miu_walk = np.append(miu_walk,miu_prime)
            l_walk = np.append(l_walk, l_prime)
        else:
            Q_walk = np.append(Q_walk,Q_walk[i])
            miu_walk = np.append(miu_walk,miu_walk[i])
            l_walk = np.append(l_walk, l_init)
            
#plt.show
#q vs miu

max_l = np.argmax(l_walk)
best_Q = Q_walk[max_l]
best_miu = miu_walk[max_l]

#print(np.log10(l_walk[max_l]))
#print(best_Q)
#print(best_miu)

#Se declaran valores de C y R
C = (best_Q/10)
R = 1/(best_miu*C)

print(C)
print(R)

best_y = my_model(t, best_Q, best_miu)

#Histogramas y Gráfica

min_Q = np.amin(Q_walk)
max_Q = np.amax(Q_walk)
min_miu = np.amin(miu_walk)
max_miu = np.amax(miu_walk)
grid_Q, grid_miu = np.mgrid[min_Q:max_Q:200j, min_miu:max_miu:200j]

npoints = np.size(Q_walk)
points = np.ones((npoints,2))
#print(points)
points[:,0] = Q_walk
points[:,1] = miu_walk

#Grafica valores R y C en función de la función likelihood
plt.figure()
grid_l = griddata(points, -np.log(l_walk), (grid_Q, grid_miu), method='cubic')
plt.imshow(grid_l.T, extent=(min_Q,max_Q,min_miu,max_miu), aspect='auto',origin='lower')
plt.savefig('Función.png')

#Histogramas Q y miu

plt.figure()
plt.subplot(2, 1, 1)
count, bins, ignored = plt.hist(Q_walk, 50, normed=True) 
plt.title('Histogramas Q Y miu')
plt.ylabel('Q')
plt.xlim(-100,350)

plt.subplot(2, 1, 2)
count, bins, ignored = plt.hist(miu_walk, 50, normed=True)
plt.xlabel('Carga (C)')
plt.ylabel('Miu')
plt.xlim(0,10)

plt.savefig('HistogramasQ-miu.png')

#---------------------------------------------
#Histogramas R Y C 
plt.figure()
plt.subplot(2, 1, 1)
Vo=10.0
Cwalk= Q_walk/Vo

count, bins, ignored = plt.hist(Cwalk, 50, normed=True) 
plt.title('Histogramas R Y C')
plt.ylabel('Capacitancia (C) F')
plt.xlim(-10,50)

plt.subplot(2, 1, 2)

R=[]
for i in Cwalk:
    Ri= (1.0/i*best_miu)
    R.append(Ri)
    
count, bins, ignored = plt.hist(R, 50, normed=False)
plt.xlabel('Carga (C)')
plt.ylabel('Resistencia (R) Ohm')
plt.xlim(-1,1)

plt.savefig('HistogramasRC.png')

#------------------------------------------------
#Gráfica de Datos y Modelo creado para R Y C
plt.figure()
fig = plt.scatter(t,y)
#'ko-', linewidth = 2, label = 'Carga')
plt.xlabel('Carga')
plt.ylabel('Tiempo')
plt.title('Gráfica Datos y Modelo ', fontsize = 20, color = 'k')

fig2= plt.plot(t,best_y,'g-', linewidth = 3, label = 'C = 10.56, R= 5.93')
plt.hold(True)
legend = plt.legend(loc="upper center", shadow = True, fontsize = 'x-large')
plt.savefig('GraficaDatosModelo.png')
