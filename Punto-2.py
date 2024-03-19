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