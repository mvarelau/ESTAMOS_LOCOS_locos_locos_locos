#8-5
def calcular_potencia_dos(n):
    resultado = 1
    for _ in range(n):
        resultado *= 2
    return resultado

n = int(input("Ingrese un número entero para calcular 2^n: "))
if n < 0:
    print("El exponente debe ser un número entero no negativo.")
else:
    resultado = calcular_potencia_dos(n)
    print(f"2^{n} es igual a {resultado}")

