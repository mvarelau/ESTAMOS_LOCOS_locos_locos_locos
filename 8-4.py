#8-4
def calcular_factorial(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

n = int(input("Ingrese un número natural: "))
if n < 1:
    print("El número debe ser mayor o igual a 1.")
else:
    print("Número\tFactorial") #se pone \t para que se vea como una tabla
    for n in range(1, n + 1):
        factorial = calcular_factorial(n)
        print(f"{n}\t{factorial}")
