# Hola queridos, esto podria tomarse como un nivel más avanzado a del primer modulo de graficos 3D, por lo que
# el proposito de este es orientar y disfrutar de jugar con codigo aprendiendo a hacer graficos tan interesantes como 
# los presentes en este repositorio. 

# se estara actualizando...

# Graficas con porcentaje en 3D, para implementación en proyectos tecnicos.

# Como primera instancia tenemos que importar todas la variables y palabras reservadas que vayamos a utilizar.
import numpy as np
from matplotlib import pyplot
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

#-----------------------------------------------
# Grafico basico de barras en 3D. 
#-----------------------------------------------


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Tenemos en las proximas lineas de codigo arrays con datos que utilizaremos como ejemplo para el desarrollo
# de este primer formato de grafica.

# Indicamos el nombre de paises como información de ejemplo en este proyecto.
paises = ['Japon','España','Rusia','Inglaterra']

# Indicamos valores arbitrarios cualquiera, como por ejemplo.
valores = [1000,4500,2000,1500]
# Coordenadas de cada barra, como ahora nos moveremos en un entorno tridimencional, la forma de transferir datos 
# en la grafica, seran un poco diferentes
x = [0,1,2,3]
y = [0,1,2,3]
z = np.zeros(4)

dx = np.ones(4) #ANCHURA DE CADA BARRA
dy = np.ones(4) #PROFUNDIDAD DE CADA BARRA
valores = [1000,4500,2000,1500] #ALTURA DE CADA BARRA

# Indicamos los colores de nuestra preferencia para utilizar.
colores = ['#30002c','#6e0dc9d2','#30002c','#6e0dc9d2']

# Utilizamos la variable title para indicar un titulo en la pestaña de la grafica, valga la redundancia.
pyplot.title ('Grafico de barras en 3D.')

# Se utiliza la variable bar, para determinar el tipo de grafico que requerimos, en este caso va ser un grafico de barras.
ax.bar3d (x, y, z, dx, dy, valores, color=colores)

# Por ultimo se utiliza "plt.show", para ejecutar nuestro grafico en una ventana emergente individual.
plt.show()

#-----------------------------------------------
# Algo no tan basico en 3D. 
#-----------------------------------------------

#https://www.geeksforgeeks.org/3d-surface-plotting-in-python-using-matplotlib/

# Creating dataset
x = np.outer(np.linspace(-3, 3, 32), np.ones(32))
y = x.copy().T # transpose
z = (np.sin(x **2) + np.cos(y **2) )
 
# Creating figure
fig = plt.figure(figsize =(14, 9))
ax = plt.axes(projection ='3d')
 
# Creating color map
my_cmap = plt.get_cmap('hot')
 
# Creating plot
surf = ax.plot_surface(x, y, z,
                       rstride = 8,
                       cstride = 8,
                       alpha = 0.8,
                       cmap = my_cmap)
cset = ax.contourf(x, y, z,
                   zdir ='z',
                   offset = np.min(z),
                   cmap = my_cmap)
cset = ax.contourf(x, y, z,
                   zdir ='x',
                   offset =-5,
                   cmap = my_cmap)
cset = ax.contourf(x, y, z,
                   zdir ='y',
                   offset = 5,
                   cmap = my_cmap)
fig.colorbar(surf, ax = ax,
             shrink = 0.5,
             aspect = 5)
 
# Adding labels
ax.set_xlabel('X-axis')
ax.set_xlim(-5, 5)
ax.set_ylabel('Y-axis')
ax.set_ylim(-5, 5)
ax.set_zlabel('Z-axis')
ax.set_zlim(np.min(z), np.max(z))
ax.set_title('3D surface having 2D contour plot projections')
 
# show plot
plt.show()