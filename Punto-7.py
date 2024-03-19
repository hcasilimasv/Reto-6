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