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