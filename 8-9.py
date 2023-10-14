import math 
def aproximacion_seno(x: float, n:int) -> float:
  a: float= 0
  for i in range(n):
     coeficiente = (-1) ** i
     exponente = 2 * i + 1
     factorial = math.factorial(exponente)
     
     a += coeficiente * (x ** exponente) / factorial
  return a

def descubrir_n(x:float, n:int) -> float:
  aproximacion = aproximacion_seno(x,n)
  exacto = math.sin(x)
  while (abs(aproximacion - exacto)/exacto)*100>0.1:
    aproximacion = aproximacion_seno(x,n)
    n+=1
  return(n)

if __name__=="__main__":
  x=float(input("Ingrese un numero real: "))
  n=int=1
  n=descubrir_n(x,n)
  aprox=aproximacion_seno(x,n)
  exac= math.sin(x)
  print(f"Esta es la aproximación de Sen {x}: {aprox}")
  print(f"Este es el valor exacto de Sen {x}: {exac}")
  print(f"Este es el nmero de repeticiones necesarias para que el npumero aproximado de lo más cercano al exacto: {n}")


