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











