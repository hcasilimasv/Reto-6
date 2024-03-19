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
print("El area total del la figura es " + str(area_t) + "")
per_t = per(a, b, r)
print("El perimetro total del la figura es " + str(per_t) + "")



def carne (n:float, m:float, k:float):
    return (n*6) + (m*7) + (k)
if __name__ == "__main__":
    n = float(input("Escribir la cantidad de gallinas que posees"))
    m = float(input("Escribir la cantidad de gallos que posees"))
    k = float(input("Escribir la cantidad de pollitos que posees"))
carne_t = carne(n, m, k)
print("la cantidad de carne que posees en total es " + str(carne_t) + " kilogramos")



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



def prestamo (c:float, i:float, n:float):
    return c * (1 + i/100) ** n
if __name__ == "__main__":
    c = float(input("Escriba la cantidad que desea prestar"))
    i = float(input("Escriba la tasa de interes que desea aclarando que el maximo es 100"))
    n = float(input("Escriba la cantidad de meses para pagar el prestamo"))
v_prestamo = prestamo(c, i, n)
print("El valor total del prestamo es de " + str(v_prestamo) + " pesos")



def covid_19 (c, d):
    return c * (2 * d)
if __name__ == "__main__":
    c = float(input("Escriba el numero total de contagiados"))
    d = float(input("Escriba el total de dias transcurridos"))
contiagados = covid_19(c, d)
print("El numero total de contagiados despues de " + str(d) + " dias es " + str(contiagados) + "")



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