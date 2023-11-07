'''
Sistema de calificaciones: Crear un sistema de calificaciones de
la siguiente manera:
'''
calificacion = int(input('Ingrese una calificación entre 0-10'))
if 9 <= calificacion <= 10:
    print(f'A')
elif 8 <= calificacion < 9:
    print(f'B')
elif 7 <= calificacion <8 :
    print(f'C')
elif 6 <= calificacion <7 :
    print(f'D')
elif 0 <= calificacion <6 :
    print(f'F')
else:
    print('El valor ingresado es incorrecto')
