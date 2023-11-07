'''
Etapas de vida: El usuario ingresará su edad y se imprimirá
la etapa de su vida en una breve oración
'''
edad = int(input('Ingrese su edad: '))
if edad > 0 and edad <= 9 :
    print(f'La infancia es increíble y bella')
elif edad >= 10 and edad <= 19 :
    print(f'Tienes muchos cambios, mucho que estudiar')
elif edad >=20 and edad <= 29 :
    print(f'Amor y comienza el trabajo')
elif edad >=30 and edad <=39 :
    print(f'A disfrutar de la familia y los amigos')
else:
    print(f'Etapa de vida no reconocida')