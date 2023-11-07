'''
Intercambiar el valor de dos variables
'''
a = 15
b = 3
c = 0
print(f'El valor de la variable a es: {a}')
print(f'El valor de la variable b es: {b}')
respuesta= input('Escriba Sí, si quiere intercambiar el valor de las variables a y b')
if respuesta == 'Sí':
    c = a
    a = b
    b = c
print(f'El nuevo valor de a es: {b}')
print(f'El nuevo valor de b es: {a}')

