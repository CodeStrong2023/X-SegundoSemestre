'''
Estación del año: Al ingresar un valor del 1 al 12
se le dirá al usuario a qué estación del año pertenece el valor
ingresado, correspondiendo 1 al mes de Enero y así sucesivamente.
'''
mes = int(input('Ingrese un mes del año (1-12): '))
estacion = None
if mes == 1 or mes == 2 or mes == 3:
    estacion = 'Verano'
elif mes == 4 or mes == 5 or mes == 6:
    estacion = 'Otoño'
elif mes == 7 or mes == 8 or mes == 9:
    estacion = 'Invierno'
elif mes == 10 or mes == 11 or mes == 12:
    estacion = 'Primavera'
else:
    estacion = 'Error, no hay número para ese mes'
print(f' Para el mes {mes} la estación es: {estacion}')
