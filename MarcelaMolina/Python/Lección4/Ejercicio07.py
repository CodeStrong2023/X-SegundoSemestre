# Ejercicio 7: Juego adivina el numero
# Realizar un juego para adivinar un numero. Para ello se debe
# generar un numero aleatorio entre 1 - 100, y luego ir pidiendo
# numeros indicando "es mayor" o "es menor" segun sea mayor o menor
# con respecto a N. El proceso termina cuando el usuario acierta
# y alli se debe mostrar el numero de intentos.

import random
aleatorio = random.randint(0, 100)
contador = 0
print("\t.:Juego Adivina el número:.")

while True:
    numero = int(input("Ingrese un número: "))
    contador += 1
    if numero > aleatorio:
        print("\tNo es el número, ingrese un número menor")
    elif numero < aleatorio:
        print("\tNo es el número, ingrese un número mayor")
    else:
        print(f"FELICIDADES, acabas de adivinar el número {aleatorio}")
        break # Rompe el ciclo y el bucle
print(f"\tNumero de intentos: {contador}")
