# ESTAMOS_LOCOS_locos_locos_locos
Estresante. Pero enviciador  😶‍🌫️
## Punto 1
Imprimir un listado con los números del 1 al 100 cada uno con su respectivo cuadrado.
* Para este punto utilicé una iteracion hasta 100 con un range y posteriormente definí el cuadrado para cada iteración
```python
for a in range(1,101):
  cuadrado=a**2
  print(f"{a} - {cuadrado}")
```
Ver documento [8-1.py](/8-1.py)

## Punto 2
Imprimir un listado con los números impares desde 1 hasta 999 y seguidamente otro listado con los números pares desde 2 hasta 1000.
* Creé dos funciones para poder hacer la impresión mas ordenada. Una en la que se imprimen solo los números impares del 1 al 999, esto con un range que suma 2 cada iteración, y como comienza en 1 arroja solo los impares. Y por otro lado hice parcticamente lo mismo solo que hasta el 1000 empezando en 2 para que la suma de 2 cada vez, sea par.
```python
def impares():
  print("Estos son los números impares hasta el 999: ")
  for a in range(1, 1000, 2):
    print(a)

def pares():
  print("Estos son los números pares hasta el 1000")
  for b in range(2, 1001, 2):
    print(b)

impares()
pares()
```
Ver documento [8-2.py](/8-2.py)

## Punto 3
Imprimir los números pares en forma descendente hasta 2 que son menores o iguales a un número natural n ≥ 2 dado
* En este punto utilicé un range que resta cada vez que empieza en n y termina en 0, para cada iteración se resta 1 (esto hace que la lista se imprima en orden descendente) y para cada npumero de la lista se decartan los que son impares.
```python
def imprimir_pares_descendentes(n):
    if n < 2:
        print("El número debe ser mayor o igual a 2.")
    else:
        for b in range(n, 1, -1):
            if b % 2 == 0:
                print(b)
n = int(input("Ingrese un número natural (n ≥ 2): "))
print("Números pares descendentes hasta 2:")
imprimir_pares_descendentes(n)

```
Ver documento [8-3.py](/8-3.py)

## Punto 4
Imprimir los números de 1 hasta un número natural n dado, cada uno con su respectivo factorial
* Primero defini una variable que es donde se va a ir guardando el resuldado de las multiplicaciones con un range que emmpieza en 1 y termina en n, la variable se actualiza como la multiplicación anterior, multiplicado el número siguiente. Despues utilicé un if para que el usuario no pueda ingresar valores negativos.
* Bueno, para imprimirlo utilicé `\t` que la verdad ni se cómo se llama, pero sirve para que todo quede en columnas más bonito.
- Disclaimer: traté de utilizarlo en las tablas pero no pude 😕😔

```python
def calcular_factorial(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

if __name__== "__main__":
  n = int(input("Ingrese un número natural: "))
  if n < 1:
      print("El número debe ser mayor o igual a 1.")
  else:
      print("Número\tFactorial") #se pone \t para que se vea como una tabla
      for n in range(1, n + 1):
          factorial = calcular_factorial(n)
          print(f"{n}\t{factorial}")
```
Ver documento [8-4.py](/8-4.py)

## Punto 5
Calcular el valor de 2 elevado a la potencia n usando ciclos for
* Un número elevado a un apotencia es ese número multiplicado por si mismo n veces. Con ayuda de un range que empieza en 1 y termina en n, inicialicé a cada uno de los números en la lista como 2 y depues en una variable que ya había creado, la actualizo como i*i.
```python
def calcular_potencia_dos(n:int):
    resultado = 1
    for i in range(1,n+1):
         i= 2
         resultado *= i
    return resultado


n = int(input("Ingrese un número entero para saber 2^n: "))
resultado = calcular_potencia_dos(n)
print(f"2^{n} es igual a {resultado}")

```
Ver documento [8-5.py](/8-5.py)

## Punto 6
Leer un número natural n, leer otro dato de tipo real x y calcular x^n usando ciclos for. 
* Este punto es parecido al anterior solo que no hay necesidad de innicializar la i como 2, si no que la variable de almacenamiento se va a guardar como ese número multiplicado coo si mismo y lo hace la cantidad de veces que de la lista.
```python
def potencias():
  n=int(input("Ingrese un npumero natural: "))
  x=float(input("Ingrese otro número natural: "))
  resultado = 1
  for i in range(1,n+1):
    resultado *= x
  print(f"El resultado de {x}^{n} es igual a {resultado}")


potencias()
```
Ver documento [8-6.py](/8-6.py)
## Punto 7
Diseñe un programa que muestre las tablas de multiplicar del 1 al 9.
- La verdad estuvo bien bonito hacer este ejercicio.
* Aquí usé un while para que la iteración sea finita y se hagan las tablas solo hasta el 9. Dentro de while puse un range que empieza en uno y acaba en 10 e inicializo un variable como `n*=a` para que se guarden los multiplos de ese número de hasta el 10. Y despues de eso actualicé la variable n ccomo `n*=1`
```python

n:int=1
def multiplos(n):
  while n<=10:
    for a in range(1,11):

        tablas= n* a
        print(f"{n} * {a} = {tablas}")
    n+=1
    print(f"Esta es la tabla del {n}")
multiplos(n)
```
Ver documento: [8-7.py](/8-7.py)
Diseñar una función que permita calcular una aproximación de la función exponencial alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Maclaurin. Nota: use math para traer la función exponencial y mostrar la diferencia entre el valor real y la aproximación.
* Lo primero fue hacer una funión en la que incialicé una variable para almacenar lo que se iba a sumar, luego utilicé un range que empieza en 0 y termina en n, y definí una variable con la formula de exponencial de la serie de Maclaurin.
![image](https://github.com/mvarelau/ESTAMOS_LOCOS_locos_locos_locos/assets/141885396/0c39ecba-e2ac-4aa6-b834-1dba987925cf)

```python
from math import*
def aproximacion_exponencial(x: float, n:int) -> float:
  suma: float= 0
  for i in range(n+1):
    a = (x**i)/ factorial(i)

    suma += a
  return suma


```
* Después hice otra función en la que busco el numero de iteraciones necesarias para que el resultado de la forula exponencial de Maclaurin sea lo más seracano al resultado real. Lo hice con un range y la siguiente ecuación: `|(aproximacion - exacto|/exacto)*100>0.1`
```python

def descubrir_n(x:float, n:int):
   aproximacion = aproximacion_exponencial(x,n) 
   exacto = exp(x)
   while (abs(aproximacion - exacto)/exacto)*100>0.1:
     aproximacion = aproximacion_exponencial(x,n)
     n+=1
   return(n)
````
* Y ya por último inicialice las variables x y n y pedí printear.
```python
if __name__=="__main__":
  x=float(input("Ingrese un numero real: "))
  n:int=1
  n=descubrir_n(x,n)
  aprox=aproximacion_exponencial(x,n)
  real=exp(x)
  print(f"Esta es la aproximación de e^{x}: {aprox}")
  print(f"Esta es el valor real de e^{x}: {real}")
  print(f"Esta es el número de iteraciones que se necesita para que el porcentaje de la diferencia entre el valor real y el aproximado sea menor que 0,1: {n}")
```
- En el reto anterior casi no usé el main, porque no entendia bien cómo funcionaba, pero en este ya traté de usarlo lo más posible :)

 
Ver documento: [8-8.py](/8-8.py)
## Punto 9 y 10
Diseñar una función que permita calcular una aproximación de la función seno alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Maclaurin. Nota: use math para traer la función seno y mostrar la diferencia entre el valor real y la aproximación.
- Para el punto 9 y 10 lo único que hhice fue copiar el 8 y cambiar la fórmula y lso nombres de las variables, porque de resto funciona exactamente igual.
### 9
![image](https://github.com/mvarelau/ESTAMOS_LOCOS_locos_locos_locos/assets/141885396/b1415005-d7d3-4b13-852f-61d51894cecb)

```python
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
```
Ver documento: [8-9.py](/8-9.py)
### 10
![image](https://github.com/mvarelau/ESTAMOS_LOCOS_locos_locos_locos/assets/141885396/24618f0d-3876-4620-8000-acbef315261f)
```python
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
```
Ver documento: [8-9.py](/8-9.py)








