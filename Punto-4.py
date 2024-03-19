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