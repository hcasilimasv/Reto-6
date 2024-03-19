def covid_19 (c, d):
    return c * (2 * d)
if __name__ == "__main__":
    c = float(input("Escriba el numero total de contagiados"))
    d = float(input("Escriba el total de dias transcurridos"))
contiagados = covid_19(c, d)
print("El numero total de contagiados despues de " + str(d) + " dias es " + str(contiagados) + "")