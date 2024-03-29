'''
Sintaxis de range(inicio<opcional>, fin<requerido>, incremento <opcional>)

Ejercicio 1: Iterar un rango de 0 a 10 e imprimir n° divisibles por 3
'''

#Ejercicio 1: Iterar un rango de 0 a 10 e imprimir números divisibles entre 3
#Ejemplo de ejecución:0,3,6,9
print('Rango de 0 a 10 con números divisibles por 3')
for i in range(11):
    if i % 3 ==0:
         print(i)


#Ejercicio 2: Crear un rango de n° de 2 a 6 e imprimirlos

print('Rango de 2 a 6')
rango = range(2, 7)
for i in rango:
    print(i)

'''
Ejercicio 3: Crear un rango de 3 a 10 pero con un incremento de 2 en 2
'''
print("Rango de 3 a 10, incremento de 2 en 2")
for i in range(3, 11, 2):
    print(i)
