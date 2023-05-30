import numpy as np
from matplotlib import pyplot
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

#-----------------------------------------------
# Grafico basico de barras. 
#-----------------------------------------------

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Tenemos en las proximas lineas de codigo arrays con datos que utilizaremos como ejemplo para el desarrollo
# de este primer formato de grafica.

# Indicamos el nombre de paises como información de ejemplo en este proyecto.
paises = ['Japon','España','Rusia','Inglaterra']

# Indicamos valores arbitrarios cualquiera, como por ejemplo.
valores = [1000,4500,2000,1500]
#COORDENADA DE CADA BARRA
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