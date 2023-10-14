#8-5
def calcular_potencia_dos(n):
    resultado = 1
    for i in range(1,n+1):
        resultado *= 2
    return resultado

n = int(input("Ingrese un número entero para calcular 2^n: "))
resultado = calcular_potencia_dos(n)
print(f"2^{n} es igual a {resultado}")

