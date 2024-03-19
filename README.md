# Reto 6

##### 1. Dado la figura de la imagen, desarrolle:

[![Captura.png](https://i.postimg.cc/Cx2HPfDJ/Captura.png)](https://postimg.cc/MnyQXH9j)

##### * Una función matemática para calcular el volumen y el área superficial.
##### * Cree dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado `r1`, `r2` y `h`.
##### * Revise como utilizar el valor de pi usando import math y math.pi

```
import math
def vol (r_1:float, r_2:float,h:float):
   return ((4/3) *math.pi * r_1**3) + ((1/3) * math.pi * r_2**2 * h)
def are (r_1:float,r_2:float,h:float):
   return (4 * math.pi * r_1**2) + (math.pi * r_2 * (r_2 + math.sqrt(h**2 + r_2**2)))
if __name__ == "__main__":
   r_1 = float(input("Escribir el valor del radio de la esfera"))
   r_2 = float(input("Escribir el valor del radio del cono"))
   h = float(input("Escribir el valor de la altura del cono"))
   vol_t = vol(r_1,r_2,h)
   print("El volumen total del la esfera y el cono es " + str(vol_t) + "")
   are_t = are(r_1,r_2,h)
   print("El area total del la esfera y el cono es " + str(are_t) + "")
```


##### 2. Dado la figura de la imagen, desarrolle:

[![Captura2.png](https://i.postimg.cc/XJsvL9BY/Captura2.png)](https://postimg.cc/ft0ZTtvG)

##### * Una función matemática para calcular el área y el perimetro.
##### * Cree dos funciones en python para calcular los valores antes establecidos, al ingresar por teclado `r`, `a` y `b`.
##### * Revise como utilizar el valor de pi usando import math y math.pi

```
import math
def are (a:float, b:float, r:float):
    return (b*a) + 2*(math.pi*r)
def per (a:float, b:float, r:float):
    return (2*(b+a)) + (2*math.pi*r)
if __name__ == "__main__":
    a = float(input("Escribir el valor de la altura de la rectangulo"))
    b = float(input("Escribir el valor de la base de la rectangulo"))
    r = float(input("Escribir el valor del radio de los dos circulos"))
area_t = are(a, b, r)
print("El area total del la figura es " + str(are_t) + "")
per_t = per(a, b, r)
print("El perimetro total del la figura es " + str(per_t) + "")
```


##### 3. Diseñe una función que calcule la cantidad de carne de aves en kilos si se tienen N gallinas, M gallos y K pollitos cada uno pesando 6 kilos, 7 kilos y 1 kilo respectivamente.

```
def carne (n:float, m:float, k:float):
    return (n*6) + (m*7) + (k)
if __name__ == "__main__":
    n = float(input("Escribir la cantidad de gallinas que posees"))
    m = float(input("Escribir la cantidad de gallos que posees"))
    k = float(input("Escribir la cantidad de pollitos que posees"))
carne_t = carne(n, m, k)
print("la cantidad de carne que posees en total es " + str(carne_t) + " kilogramos")
```


##### 4. Mi mamá me manda a comprar P panes a 300 cada uno, M bolsas de leche a 3300 cada una y H huevos a 350 cada uno. Hacer un programa que me diga las vueltas (o lo que quedo debiendo) cuando me da un billete de B pesos.

```
def buy (p:float, m:float, h:float, b):
    return - ((p * 300) + (m * 3300) + (h * 300)) + b
if __name__ == "__main__":
    p = float(input("Escribir la cantidad de panes a comprar"))
    m = float(input("Escribir la cantidad de leche a comprar"))
    h = float(input("Escribir la cantidad de huevos a comprar"))
    b = float(input("Escribir la cantidad con la que va pagar"))
cambio = buy(p, m, h, b)
if cambio >= 0:
   print("sus vueltas son " + str(cambio) + " pesos")
else:
    print("mijo con eso no alcanza comprar lo que quieres, es mas debe "+ str(cambio) + " pesos")
```


##### 5. Haga un programa que utilice una función para calcular el valor de un préstamo `C` usando interés compuesto del `i` por `n` meses.

```
def prestamo (c:float, i:float, n:float):
    return c * (1 + i/100) ** n
if __name__ == "__main__":
    c = float(input("Escriba la cantidad que desea prestar"))
    i = float(input("Escriba la tasa de interes que desea aclarando que el maximo es 100"))
    n = float(input("Escriba la cantidad de meses para pagar el prestamo"))
v_prestamo = prestamo(c, i, n)
print("El valor total del prestamo es de " + str(v_prestamo) + " pesos")
```


##### 6. El número de contagiados de Covid-19 en el país de NuncaLandia se duplica cada día. Hacer un programa que diga el número total de personas que se han contagiado cuando pasen `D` días a partir de hoy, si el número de contagiados actuales es `C`.

```
def covid_19 (c, d):
    return c * (2 * d)
if __name__ == "__main__":
    c = float(input("Escriba el numero total de contagiados"))
    d = float(input("Escriba el total de dias transcurridos"))
contiagados = covid_19(c, d)
print("El numero total de contagiados despues de " + str(d) + " dias es " + str(contiagados) + "")
```


##### 7. Escriba un programa que pida 5 números reales y calcule las siguientes operaciones usando una función para cada una:

##### * El promedio
##### * La mediana
##### * El promedio multiplicativo (multilplica todos y luego calcula la raíz de la cantidad de operandos)
##### * Ordenar los números de forma ascendente
##### * Ordenar los números de forma descendente
##### * La potencia del mayor número elevado al menor número
##### * La raíz cúbica del menor número

```
def promedio (a:float, b:float, c:float, d:float, e:float):
    return (a + b + c + d + e) / 5
def mediana (a:float, b:float, c:float, d:float, e:float):
    return (a + b + c + d + e) // 5
def pro_multi (a:float, b:float, c:float, d:float, e:float):
    return (a * b * c * d * e) ** (1/5)
def ascendente (a:float, b:float, c:float, d:float, e:float):
    return sorted((a, b, c, d, e))
def descendente (a:float, b:float, c:float, d:float, e:float):
    return sorted((a, b, c, d, e), reverse = True)
def potencia (a:float, b:float, c:float, d:float, e:float):
    return max (a, b, c, d, e) ** min (a, b, c, d, e)
def raiz_cubica (a:float, b:float, c:float, d:float, e:float):
    return min (a, b, c, d, e) ** (1/3)
if __name__ == "__main__":
    a = float(input("Escriba el primer numero"))
    b = float(input("Escriba el segundo numero: "))
    c = float(input("Escriba el tercer numero: "))
    d = float(input("Escriba el cuarto numero: "))
    e = float(input("Escriba el quinto numero: "))
cal_promedio = promedio(a, b, c, d, e)
cal_mediana = mediana(a, b, c, d, e)
cal_pro_multi = pro_multi(a, b, c, d, e)
cal_ascendente = ascendente(a, b, c, d, e)
cal_descendente = descendente(a, b, c, d, e)
cal_potencia = potencia(a, b, c, d, e)
cal_raiz_cubica = raiz_cubica(a, b, c, d, e)
print("El promedio es " + str(cal_promedio) + "")
print("La mediana es " + str(cal_mediana) + "")
print("El promedio multiplicativo es " + str(cal_pro_multi) +"")
print("El orden de los numeros en forma ascendete es " + str(cal_ascendente) + "")
print("El orden de los numeros en forma descendente es " + str(cal_descendente) + "")
print("La potencia del mayor numero elevado al menor numero es " + str(cal_potencia) + "")
print("La raiz cubica del menor numero es " + str(cal_raiz_cubica) + "")
```


##### 8. Para el punto anterior incluir las funciones en un archivo independiente e importarlas para su uso.

###### R: El archivo esta adjuntado en la parte de arriba


##### 9. Consultar qué es y cómo funciona pip en python

###### R: ¿Qué es pip?

###### Pip es un sistema de gestión de paquetes utilizado para instalar y administrar paquetes de software escritos en Python. Se ha convertido en la herramienta estándar para la gestión de dependencias en proyectos Python.

##### ¿Cómo funciona pip?

###### Pip funciona buscando e instalando paquetes desde el Python Package Index (PyPI), un repositorio central que alberga miles de paquetes de código abierto desarrollados por la comunidad Python.

##### Principales funcionalidades de pip:

###### Instalación de paquetes: Puedes instalar paquetes específicos o conjuntos de paquetes utilizando comandos como pip install nombre_paquete o pip install -r requirements.txt.

###### Actualización de paquetes: Puedes actualizar paquetes a la última versión disponible con el comando pip install --upgrade nombre_paquete.

###### Desinstalación de paquetes: Puedes eliminar paquetes que ya no necesitas con el comando pip uninstall nombre_paquete.

###### Búsqueda de paquetes: Puedes buscar información sobre paquetes específicos o encontrar paquetes que satisfagan tus necesidades con el comando pip search nombre_paquete.

###### Manejo de dependencias: Pip te permite instalar automáticamente las dependencias de un paquete con el comando pip install nombre_paquete[dependencias].

##### Ventajas de usar pip:

###### Facilita la instalación y gestión de paquetes en proyectos Python.

###### Promueve la reutilización de código y la colaboración entre desarrolladores.

###### Permite mantener tus proyectos actualizados con las últimas versiones de los paquetes.

###### Ofrece una amplia variedad de paquetes para diferentes funcionalidades.


##### 10. Hacer un listado de módulos populares para python que se puedan instalar com pip y consultar cómo instalarlos.

###### R: Módulos populares de Python que se pueden instalar con pip:
###### 1. NumPy: Biblioteca fundamental para computación científica con Python. Permite realizar operaciones matemáticas con matrices y vectores de forma eficiente.

###### 2. Pandas: Herramienta poderosa para análisis de datos. Facilita la manipulación, limpieza y visualización de datos.

###### 3. Matplotlib: Biblioteca para la creación de gráficos y visualizaciones de datos. Ofrece una amplia variedad de opciones para personalizar y ajustar tus gráficas.

###### 4. Scikit-learn: Biblioteca de aprendizaje automático con una amplia gama de algoritmos y herramientas para la clasificación, regresión, clustering y otras tareas.

###### 5. TensorFlow: Framework de código abierto para aprendizaje profundo. Permite desarrollar e implementar modelos de aprendizaje profundo de forma eficiente.

###### 6. Django: Framework web robusto y flexible para la creación de aplicaciones web con Python.

###### 7. Flask: Microframework web ligero y fácil de usar para el desarrollo de aplicaciones web simples.

###### 8. Requests: Biblioteca para realizar peticiones HTTP y consumir APIs de forma sencilla.

###### 9. BeautifulSoup: Biblioteca para el análisis y extracción de datos de páginas web.

###### 10. Selenium: Herramienta para automatizar la interacción con navegadores web y realizar pruebas de aplicaciones web.

##### 1. Instalación básica:
```
pip install nombre_modulo
```

##### 2. Instalación con opciones:
```
pip install nombre_modulo[opciones]
```

##### 3.  Actualización de módulos:
```
pip install --upgrade nombre_modulo
```

##### 4. Desinstalación de módulos
```
pip uninstall nombre_modulo
```

##### Recomendaciones:

###### Es importante elegir el módulo adecuado para la tarea que deseas realizar. Investiga la documentación del módulo antes de instalarlo. Mantén tus módulos actualizados a la última versión. Utiliza un entorno virtual para aislar las dependencias de cada proyecto.

#### Conclusión:

##### Estos son solo algunos de los muchos módulos populares que se pueden instalar con pip. La gran variedad de módulos disponibles te permite ampliar las funcionalidades de Python y desarrollar aplicaciones para diferentes áreas. Familiarizarse con el uso de pip te permitirá aprovechar al máximo las capacidades de Python y te facilitará el desarrollo de aplicaciones robustas y escalables.
