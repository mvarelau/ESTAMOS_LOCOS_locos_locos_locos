#10-8
import math 
def aproximacion_arcotan(x: float, n:int) -> float:
  a: float= 0
  for i in range(n):
     coeficiente = (-1) ** i
     exponente = 2 * i + 1
     
     a += coeficiente * (x ** exponente) / exponente
  return a

def descubrir_n(x:float, n:int) -> float:
  aproximacion = aproximacion_arcotan(x,n)
  exacto = math.atan(x)
  while (abs(aproximacion - exacto)/exacto)*100>0.1:
    aproximacion = aproximacion_arcotan(x,n)
    n+=1
  return(n)


x=float(input("Ingrese un número real: "))
n:int=1
n=descubrir_n(x,n)
arcotan=aproximacion_arcotan(x,n)
exac= math.atan(x)
print(f"Esta es la aproximación de Sen {x}: {arcotan}")
print(f"Este es el valor exacto de Sen {x}: {exac}")
print(f"Este es el nmero de repeticiones necesarias para que el número aproximado de lo más cercano al exacto: {n}")




