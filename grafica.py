# Graficas con porcentaje, para implementación en proyectos tecnicos.

# Como primera instancia tenemos que importar todas la variables y palabras reservadas que vayamos a utilizar.
from matplotlib import pyplot
import matplotlib.pyplot as plt

#-----------------------------------------------
# Grafico basico de barras 
#-----------------------------------------------

# Tenemos en las proximas lineas de codigo arrays con datos que utilizaremos como ejemplo para el desarrollo
# de este primer formato de grafica.

# Indicamos el nombre de paises.
paises = ['japon','españa','rusia','inglaterra']

# Indicamos valores arbitrarios como ejemplo.
valores = [1000,4500,2000,1500]

# Indicamos los colores a utilizar.
colores = ['#30002c','#30002c','#30002c','#30002c']

# Utilizamos la variable title para indicar un titulo valga la redundancia.
pyplot.title ('wenas soy un titulo suave para poner como ejemplo')

# Se utilizar la bariable bar, para determinar qque va ser un grafico de barras.
pyplot.bar(paises, height=valores, color=colores, width=0.5)

# Por ultimo se utiliza "plt.show", para ejecutar nuestro grafico en unua ventana individual para cada uno.
plt.show()

#-----------------------------------------------
# Grafico lineal basico
#-----------------------------------------------

# Para este primer grafico linea basico, tenemos que definir dos arrays.
# Uno va ser para el eje "X" y otro para el eje "Y", los cuales nos ayudaran a determinar su comportamiento.

# "eje_y", sirve para llevar una constancia, pueden por ejemplo dias transcurridos.
# Nota: el primer array siempre se determinara en el eje x por defecto, a no ser que deseamos personalizar los ejes.
eje_x = [0,1,2,3,4,5,6,7,8,9,10]

# "linea_1", sirve para ver el patron de comportamiento de los datos que estemos podiendo en analisis, en pocas palabras
# se traduciria como los datos reales, como ejemplo la cantidad de ventas hechas por una tienda de ropa. 
linea1 = [0,1,2,3,4,5,6,7,5,9,11]

# En este apartado describimos la leyenda, donde describiremos un pequeño texto en cada eje.
plt.ylabel("Ventas realizadas por dia")
plt.xlabel("Días transcurridos")

# En esta linea personalizzamos la linea de comportamiento, como deseemos. 
plt.plot(linea1, color='#30002c', linestyle='--', marker='o')

# En este apartado personalizamos el plano de la grafica para que se adapte mejor a nuestras necesidades.
plt.subplots_adjust(wspace=0.85, bottom=0.3)
plt.show()

#-----------------------------------------------
# Grafico pastel basico :3 ñam~
#-----------------------------------------------

# Como ya hemos venido observando primero se deben de indicar los arrays a utilizar.
manzanas = [20,10,25,40]
nombres = ["Ana","Juan","Diana","Catalina"]

# En esta parte definimos los colores a travez de arrays para cada una de nuestras secciones del pastel.
colores = ["#EE6055","#60D394","#AAF683","#FFD97D","#FF9B85"]

# Aqui tenemos una funcion curiosa y es la del desfase, donde de igual manera indicamos un array e indicamos. 
# los pixeles de desfase que deseamos que contenga la sección desde el radio del pastel.
desfase = (0, 0, 0, 0.05)

# Indicamos todos los arrays anteriores para realizar la personalización del grafico.
# Nota: explote, indica el valor de desfase y autopct indica que queremos ver los respectivos porcentajes.
plt.pie(manzanas, labels=nombres, autopct="%0.1f %%", colors=colores, explode=desfase)

# Implementamos axis para determinar la forma que queremos que tenga el pastel, quitalo y te daras cuenta.
plt.axis("equal")
plt.show()
