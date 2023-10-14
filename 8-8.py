#8-8
from math import*
def aproximacion_exponencial(x: float, n:int) -> float:
  suma: float= 0
  for i in range(n+1):
    a = (x**i)/ factorial(i)

    suma += a
  return suma

def descubrir_n(x:float, n:int):
   aproximacion = aproximacion_exponencial(x,n)
   exacto = exp(x)
   while (abs(aproximacion - exacto)/exacto)*100>0.1:
     aproximacion = aproximacion_exponencial(x,n)
     n+=1
   return(n)

if __name__=="__main__":
  x=float(input("Ingrese un numero real: "))
  n:int=1
  n=descubrir_n(x,n)
  aprox=aproximacion_exponencial(x,n)
  real=exp(x)
  print(f"Esta es la aproximación de e^{x}: {aprox}")
  print(f"Esta es el valor real de e^{x}: {real}")
  print(f"Esta es el número de iteraciones que se necesita para que el porcentaje de la diferencia entre el valor real y el aproximado sea menor que 0,1: {n}")
