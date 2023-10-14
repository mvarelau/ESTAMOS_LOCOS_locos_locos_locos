#8-7

n:int=1
def multiplos(n):
  while n<=10:
    for a in range(1,11):
        
        tablas= n* a
        print(f"{n} * {a} = {tablas}")
    n+=1
    print(f"Esta es la tabla del {n}")
multiplos(n)