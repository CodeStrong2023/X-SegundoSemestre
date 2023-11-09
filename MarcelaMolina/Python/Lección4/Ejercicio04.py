# Ejercicio 4: Sumar números pares dentro de un rango
# Hacer un programa para sumar números pares dentro de un rango
# ej: suma de números pares del 2 al 30
a = int(input('Ingrese el número donde va a comenzar la suma: '))
b = int(input('Ingrese el número hasta donde quiere llegar la suma: '))
suma = 0
for i in range(a, b+1):
    if i%2 == 0: #Es si es número par
        suma += i
print(f"\nLa suma de números pares dentro del rango es: {suma}")
