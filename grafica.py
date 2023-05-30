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

# Utilizamos "between" para poder dibujar el relleno de la grafica para hacer que esta tenga una estetica mucho más agradable.
plt.fill_between(eje_x, linea1, color='#31003362')
# Con "subplots_adjust", podemos editaar parametros determinado para centrar o ajustar la posición del grafico.
plt.subplots_adjust(wspace=0.85, bottom=0.3)

# Por ultimo se utiliza "plt.show", para ejecutar nuestro grafico en una ventana emergente individual.
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

# Por ultimo se utiliza "plt.show", para ejecutar nuestro grafico en una ventana emergente individual.
plt.show()

#-----------------------------------------------
# Multiples graficos 
#-----------------------------------------------

# Okey aqui presentaremos una forma muy facil de poder tener varios graficos sin que estos se crucen o superpongan entre ellos
# para poder realizar esto, necesitamos utilizar la propiedad "subplots", donde actuara como una tabla a lo que indicaremos
# dos filas y dos columnas como valores de la propiedad "subplots" junto con el parametro "sharey =True", para compartir
# el uso de propiedades en el eje "Y".
fig, ax = plt.subplots(2, 2, sharey = True)

# Indicamos el nombre de paises como información de ejemplo en este proyecto.
paises = { 'asiaticos':[ 'Japon','China','Korea','Taiwan'], 'europeos':['Italia','Noruega','Islandia','Alemania']}

# Indicamos valores arbitrarios cualquiera, como por ejemplo.
valores = {'asia':[1000,4500,2000,1500], 'europa':[1004,3500,5080,2500]}

# Para poder acomodar estos graficos sin error alguno, tenemos que saber una cosa de ante mano y es que las posiciones de esto 
# se vera determinada con valores de un plano carteciano, ¿osea?, bueno vamos a ubicarnos a traves de coordenadas, si recordamos 
# las clases de primaria, el primer valor es el eje x "Horizontal" y el segundo es el eje y "Vertical", y si entendemos que 
# tenemos dos columnas y dos filas, osea cuatro celdas, pues hace sencillo comprender que si tenemos las coordenadas [0,0] podemos 
# intuir que sera la posición base o inicial, la cual sera en la en la primera casilla a la izquierda, entendiendo esto, sabremos que 
# si ahora tenemos las coordernadas [0,1] estaremos en la misma columna del eje x, osea la primera a la izquierda, pero una fila 
# abajo en el eje y, así sucesivamente podremos acomodar cada uno de lo graficos, puedes jugar con los valores de coordenadas si 
# no te quedo algo en claro, para que comprendas su funcionamiento de forma empirica UwU.

# Primer grafico lineal de paises asiaticos.
ax[0, 0].plot(paises['asiaticos'], valores['asia'], color = '#FCA03E')

# Primer grafico lineal de paises europeos.
ax[0, 1].plot(paises['europeos'], valores['europa'], color = '#6e0dc9d2')

# Segundo grafico de barras de paises asiaticos.
ax[1, 0].bar(paises['asiaticos'], valores['asia'], color = '#FCA03E')

# Segundo grafico de barras de paises europeos.
ax[1, 1].bar(paises['europeos'], valores['europa'], color = '#6e0dc9d2')

# Por ultimo se utiliza "plt.show", para ejecutar nuestro grafico en una ventana emergente individual.
plt.show()

