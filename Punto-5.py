def prestamo (c:float, i:float, n:float):
    return c * (1 + i/100) ** n
if __name__ == "__main__":
    c = float(input("Escriba la cantidad que desea prestar"))
    i = float(input("Escriba la tasa de interes que desea aclarando que el maximo es 100"))
    n = float(input("Escriba la cantidad de meses para pagar el prestamo"))
v_prestamo = prestamo(c, i, n)
print("El valor total del prestamo es de " + str(v_prestamo) + " pesos")