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
# Grafico de barras en 3D. 
#-----------------------------------------------

# Utilizamos el siguiente metodo que es el más coloquial, definimos una variable fig la cual
# sera en sintesis la que contendra nuestra figura o grafica principal, seguido definimos la varible ax
# con los parametros requeridos para el grafico, en este caso, le brindamos la projección 3d por medio.
# del parametro "projection='3d'" 
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Tenemos en las proximas lineas de codigo arrays con datos que utilizaremos como ejemplo para el desarrollo
# de este primer formato de grafica.


# Indicamos valores arbitrarios cualquiera, como ejemplo para este grafico.
valores = [1000,4500,2000,1500]

# Coordenadas de cada barra, como ahora nos moveremos en un entorno tridimencional, la forma de transferir datos 
# en la grafica, seran un poco diferentes
x = [0,1,2,3]
y = [0,1,2,3]
z = np.zeros(4)

# Estos valores seran aquellos que determinen los valores de anchura y profundidad del las barras, este caso los
# determinamos de manera hacendiente automatica con la propiedad "np.ones", que utiliza los valores dentro del 
# rango de 4 para poder posicionar de manera uniforma las barras, pero esto tambien se podria hacer a mano 
# modificando los valores como un array osea valores dentro de corchetes de este tipo [].
dx = np.ones(4)#ANCHURA DE CADA BARRA
dy = np.ones(4) #PROFUNDIDAD DE CADA BARRA

# Valores que determinaran la altura de las barras que son las caracteristicas que reflejaran los datos estadisticos.
valores = [1000,4500,2000,1500] #ALTURA DE CADA BARRA

# Indicamos los colores de nuestra preferencia para utilizar.
colores = ['#30002c','#6e0dc9d2','#30002c','#6e0dc9d2']

# Indicamos el nombre de paises como información de ejemplo en este proyecto.
ax.set_xlabel('Japon  España  Rusia  Inglaterra')

# Se utiliza la variable bar, para determinar el tipo de grafico que requerimos, en este caso va ser un grafico de barras
# y le añadimos la leyenda 3d, para tener el formato de grafico que deseamos, retiralo para que puedas ver su utilidad.
ax.bar3d (x, y, z, dx, dy, valores, color=colores)

# Utilizamos la variable title para indicar un titulo en la pestaña de la grafica, valga la redundancia.
pyplot.title ('Grafico de barras en 3D.')

# Por ultimo se utiliza "plt.show", para ejecutar nuestro grafico en una ventana emergente individual.
plt.show()

#-----------------------------------------------
# Grafico lineal en 3D. 
#-----------------------------------------------

#Ejemplo sustraido del Canal Pro Ciencia 
#https://youtu.be/CVM3hOrXU1U

# Al igual que en el ejemplo anterior utilizamso el mismo metodo para definir la figura/grafica requerida.
fig = plt.figure()
ax = plt.axes(projection ='3d')

# Definimos los valores de "x" y "y", para usar como ejemplo una función trigonometrica a graficar.
x = np.linspace (-4, 4, 50)
y = np.linspace (-4, 4, 50)

# Definimos la tercera variable necesasria para el entorno tridimensional, la cual tendra los valores 
# de coordenadas de "x" y "y".
def z (x,y):

    # Utilizamos la plabra reservada return, para obtener el resultado del calculo de seno (np.sin) 
    # de la raíz cuadrada (np.sqrt), de la suma de "x" elevado ^ a la 2 y "y" elevado ^ a la 2
    return np.sin(np.sqrt(x**2 + y**2))

# Utilizando la variable ax, la cual le podemos determinar el tipo de grafico despúes del ".", en este caso 
# con "plot", el cual hace referencia a un grafico de tipo lineal, y dentro de "plot", le insertamos los parametros
# de coordenadas que deseamos graficar, los cuales en ese caso son "x","y" y "z".
ax.plot(x, y, z(x,y))

# Utilizamos la variable title para indicar un titulo en la pestaña de la grafica, valga la redundancia.
pyplot.title ('Grafico lineal en 3D.')

# Por ultimo se utiliza "plt.show", para ejecutar nuestro grafico en una ventana emergente individual.
plt.show()

#-----------------------------------------------
# Gráficas lineal en 3D con puntos dispersos-scatter. 
#-----------------------------------------------

# Al igual que en el ejemplo anterior utilizamso el mismo metodo para definir la figura/grafica requerida.
fig = plt.figure()
ax = plt.axes(projection ='3d')

# Definimos los valores de "x" y "y", para usar como ejemplo una función trigonometrica a graficar.
x = np.linspace(-3, 3, 40)
y = np.linspace(-3, 3, 40) 

# Definimos la tercera variable necesasria para el entorno tridimensional, la cual tendra los valores 
# de coordenadas de "x" y "y".
def z (x,y):

    # Utilizamos la plabra reservada return, para obtener el resultado del calculo de seno (np.sin) 
    # de la raíz cuadrada (np.sqrt), de la suma de "x" elevado ^ a la 2 y "y" elevado ^ a la 2
    return (x**2 - y**2)

# Definimos a "x" y "y", con la función meshgrid para poder optener valores necesarios para el grafico 
# de tipo maya que deseamos, ya que si no realizamos esta acción los valores se pasaran como argumentos 
# bidimensionales y esto genera un error al no tener los puntos necesarios, para el tipo de grafico que deseamos implementar.
x,y= np.meshgrid(x,y)

# Utilizamos en este caso "plot_wireframe" a diferencia del anterior, el cual hace
# referencia a un grafico de tipo "cuadricula" o correctamente nombrada "Gráficas 3D puntos dispersos-scatter", 
# esto para no tener solo un bloque solido con los valores graficados, si no que los dispersa entre puntos más 
# esteticos y comprensibles, dentro de "plot", le insertamos los parametros de coordenadas que deseamos graficar, 
# los cuales en ese caso son "x","y" y "z", replanteados anteriormente por la función meshgrid.
ax.plot_wireframe(x, y, z(x,y))

# Utilizamos la variable title para indicar un titulo en la pestaña de la grafica, valga la redundancia.
pyplot.title ('Grafico lineal punteada o "dispersos-scatter" en 3D.')

# Por ultimo se utiliza "plt.show", para ejecutar nuestro grafico en una ventana emergente individual.
plt.show()

#-----------------------------------------------
# Trazado de contornos en 3D. 
#-----------------------------------------------

#Ejemplo sustraido del portal web GeeksforGeeks
#https://www.geeksforgeeks.org/3d-surface-plotting-in-python-using-matplotlib/

# Definimos los datos topograficos de la parcela
x = np.outer(np.linspace(-3, 3, 32), np.ones(32))
y = x.copy().T # transpose
z = (np.sin(x **2) + np.cos(y **2) )
 
# Creating figure
fig = plt.figure(figsize =(6, 5))
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
 
# PAra proyectar de manera 2d lo representado en el entorno 3D
ax.set_xlabel('X-axis')
ax.set_xlim(-5, 5)
ax.set_ylabel('Y-axis')
ax.set_ylim(-5, 5)
ax.set_zlabel('Z-axis')
ax.set_zlim(np.min(z), np.max(z))

# Utilizamos la variable set_title para indicar un titulo en la pestaña de la grafica, valga la redundancia.
ax.set_title('Grafico de trazado de contornos en un espacio 3D')
 
# show plot
plt.show()

#-----------------------------------------------
# Algo no tan basico en 3D. 
#-----------------------------------------------

figure=plt.figure(figsize = (6, 5))
axes = figure.add_subplot(projection ="3d")
 
random_state = np.random.RandomState(0)
x = random_state.randn(100)
y = random_state.randn(100)
z = random_state.randn(100)
color = random_state.randn(100)
size = 500 * random_state.randn(100)
 
 
scatter=axes.scatter(x,y,z,c=color,s=size,cmap='hsv', alpha=0.4)
figure.colorbar(scatter,ax=axes, shrink = 0.5)

# Utilizamos la variable title para indicar un titulo en la pestaña de la grafica, valga la redundancia.
pyplot.title ('Grafico de dispersión tridimensional.')

plt.show()

