#8-2
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