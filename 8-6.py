#8-6
def potencias():
  n=int(input("Ingrese un npumero natural: "))
  x=float(input("Ingrese otro número natural: "))
  resultado = 1
  for _ in range(n):
    resultado *= x
  print(f"El resultado de {x}^{n} es igual a {resultado}")


potencias()






