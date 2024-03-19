def carne (n:float, m:float, k:float):
    return (n*6) + (m*7) + (k)
if __name__ == "__main__":
    n = float(input("Escribir la cantidad de gallinas que posees"))
    m = float(input("Escribir la cantidad de gallos que posees"))
    k = float(input("Escribir la cantidad de pollitos que posees"))
carne_t = carne(n, m, k)
print("la cantidad de carne que posees en total es " + str(carne_t) + " kilogramos")