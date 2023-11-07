'''
Área y longitud de un circulo: Hacer un programa para ingresar el radio de un circulo
y se reporte su área y la longitud de la circunferencia.
Área = Pi * r2
Longitud = 2 * Pi * r
'''
import math
r = float(input('Ingrese el radio del círculo: '))
pi = math.pi
area = pi * r * r
longitud = 2 * pi * r
print(f'El área del círculo es: {area}')
print(f'La longitud del círculo es: {longitud}')
