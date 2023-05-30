# Graficas con porcentaje, para implementación en proyectos tecnicos.

# Como primera instancia tenemos que importar todas la variables y palabras reservadas que vayamos a utilizar.
from matplotlib import pyplot
import matplotlib.pyplot as plt

#-----------------------------------------------
# Grafico basico de barras. 
#-----------------------------------------------

# Tenemos en las proximas lineas de codigo arrays con datos que utilizaremos como ejemplo para el desarrollo
# de este primer formato de grafica.

# Indicamos el nombre de paises como información de ejemplo en este proyecto.
paises = ['japon','españa','rusia','inglaterra']

# Indicamos valores arbitrarios cualquiera, como por ejemplo.
valores = [1000,4500,2000,1500]

# Indicamos los colores de nuestra preferencia para utilizar.
colores = ['#30002c','#6e0dc9d2','#30002c','#6e0dc9d2']

# Utilizamos la variable title para indicar un titulo en la pestaña de la grafica, valga la redundancia.
pyplot.title ('wenas soy un titulo suave para poner como ejemplo')

# Se utiliza la variable bar, para determinar el tipo de grafico que requerimos, en este caso va ser un grafico de barras.
pyplot.bar(paises, height=valores, color=colores, width=0.5)

# Por ultimo se utiliza "plt.show", para ejecutar nuestro grafico en una ventana emergente individual.
plt.show()

#-----------------------------------------------
# Grafico lineal basico.
#-----------------------------------------------

# Para este primer grafico lineal basico, tenemos que definir dos arrays.
# Uno va ser para el eje "X" y otro para el eje "Y", "puesto que se reflejaran los datos en un plano cartesiano",
# los cuales nos ayudaran a determinar el comportamiento de la información y sus tendencias.

# "eje_y", sirve para llevar una constante, pueden ser por ejemplo los dias transcurridos, o algún otro tipo de unidad cuantitativa.
# Nota: el primer array siempre se determinara en el eje x por defecto, a no ser que deseamos personalizar los ejes.
eje_x = [0,1,2,3,4,5,6,7,8,9,10]

# "linea_1", sirve para ver el patron de comportamiento de los datos que estemos podiendo en analisis, en pocas palabras
# se traduciria como los datos reales, como ejemplo la cantidad de ventas hechas por una tienda de ropa. 
linea1 = [0,1,2,3,4,5,6,7,5,9,11]

# En este apartado describimos la leyenda, donde describiremos un pequeño texto en cada eje.
plt.ylabel("Ventas realizadas por dia")
plt.xlabel("Días transcurridos")

# En esta linea personalizamos la linea de comportamiento, como deseemos. 
plt.plot(linea1, color='#30002c', linestyle='--', marker='o')

# En este apartado personalizamos el plano de la grafica para que se adapte mejor a nuestras necesidades y gustos.
plt.fill_between(eje_x, linea1, color='#31003362')
plt.subplots_adjust(wspace=0.85, bottom=0.3)
plt.show()

#-----------------------------------------------
# Grafico de pastel basico :3 ñam~
#-----------------------------------------------

# Como ya hemos venido observando primero se deben de indicar los arrays a utilizar.
manzanas = [20,10,25,40]
nombres = ["Ana","Juan","Diana","Catalina"]

# En esta parte definimos los colores a travez de arrays para cada una de nuestras secciones del pastel.
colores = ["#EE6055","#60D394","#AAF683","#FFD97D","#FF9B85"]

# Aqui tenemos una funcion curiosa y es la del desfase, donde definimos una variable que guarde los valores de coordenada y con esto  
# indicamos los pixeles de desfase que deseamos que contenga la sección desde el radio del pastel, esto para emular que la sección
# esta sobresaliendo como una rebanada recién cortada.
desfase = (0, 0, 0, 0.05)

# Indicamos todos los arrays anteriores para realizar la personalización del grafico.
# Nota: explote, indica el valor de desfase y autopct indica que queremos ver los respectivos porcentajes.
plt.pie(manzanas, labels=nombres, autopct="%0.1f %%", colors=colores, explode=desfase)

# Implementamos axis para determinar la forma que queremos que tenga el pastel, quitalo y te daras cuenta cuenta con mejor comprensión.
plt.axis("equal")
plt.show()
