#8-6
def potencias():
  n=int(input("Ingrese un npumero natural: "))
  x=float(input("Ingrese otro número natural: "))
  resultado = 1
  for i in range(1, n+1):
    resultado *= x
  print(f"El resultado de {x}^{n} es igual a {resultado}")


potencias()






