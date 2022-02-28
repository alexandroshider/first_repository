#
import random 

lims=int(input("Escribe el limite superior (mayor o igual a 1):\n"))
x=int(input("Escribe el valor a adivinar (entre 1 y {}):\n".format(lims)))
limi=1
guess=random.randint(1,lims)
while guess != x:
     if guess<x:
          limi=guess
          print(f"Tu numero es mayor que {guess}")
          guess=random.randint(limi+1,lims-1)
     elif guess>x:
          lims=guess
          print(f"Tu numero es menor que {guess}")
          guess=random.randint(limi+1,lims-1)
print(f"Tu numero es {x}")
