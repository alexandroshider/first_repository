import os
import random

def clear_console():
    command="cls"
    os.system(command)

clear_console()

x = int(input("Escribe el número que el otro debe de adivinar:\n"))

clear_console()
print(type(x))
guess=int(input("Ahora el otro usuario adivine el número:\n"))
while guess != x:
    if guess>x:
        guess=int(input(f"Muy alto, elige un número menor que {guess}\n"))
    if guess<x:
        guess=int(input(f"Muy bajo, elige un número mayor que {guess}\n"))
print(f"Correcto! Tu oponente eligió {x}")


