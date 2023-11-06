        #Clase 1
#Ejercicio 1
print('Rango del 1 al 10 con numeros divisibles en 3')
for i in range(11):
    if i % 3 ==0:
        print (i)
    else:
        print('No quedan mas numeros divisibles en 3')
        
#Ejercicio 2
print('Rango del 2 al 6')
rango = range(2, 7)
for i in rango:
    print (i)
    
#Ejercicio 3
print('Rango del 3 al 10 con incremento de 2')
for i in range(3, 11, 2):
    print (i)
    
#Ejercicio Tupla
tupla = (1, 2, 3, 5, 8, 8, 13)
lista = []
for elemento in tupla:
    if elemento < 5:

            #Clase 3
#Ejercicio Seleccion
seleccionArgentina = {
    10: {"Nombre": "Lionel Messi", "Edad": 35, "Altura": 1.70, "Precio": "50 Millones", "Posicion": "Extremo Derecho"},
    11: {"Nombre": "Angel Di Maria", "Edad": 34, "Altura": 1.80, "Precio": "12 Millones", "Posicion": "Extremo Derecho"},
    24: {"Nombre": "Paulo Dybala", "Edad": 28, "Altura": 1.77, "Precio": "35 Millones", "Posicion": "Media Punta"},
    19: {"Nombre": "Nicolas Otamendi", "Edad": 34, "Altura": 1.83, "Precio": "3.5 Millones", "Posicion": "Defensa Central"},
    1: {"Nombre": "Franco Armani", "Edad": 35, "Altura": 1.89, "Precio": "3.5 Millones", "Posicion": "Arquero"},
    5: {"Nombre": "Leandro Paredes", "Edad": 29, "Altura": 1.82, "Precio": "4.5 Millones", "Posicion": "Mediocampista"},
    23: {"Nombre": "Damian Martinez", "Edad": 31, "Altura": 1.95, "Precio": "28 Millones", "Posicion": "Arquero"},
    24: {"Nombre": "Enzo Fernandez", "Edad": 22, "Altura": 1.78, "Precio": "121 Millones", "Posicion": "Mediocampista"},
    20: {"Nombre": "Alexis Mac Allister", "Edad": 24, "Altura": 1.76, "Precio": "40 Millones", "Posicion": "Mediocampista"},
    7: {"Nombre": "Rodrigo De Paul", "Edad": 29, "Altura": 1.80, "Precio": "37 Millones", "Posicion": "Mediocampista"}
}
for llave, valor in seleccionArgentina.items():
    print(llave, valor)
print("Tenemos cargados en el diccionario la cantidad de jugadores:", end="")
print(len(seleccionArgentina))


        #Clase 4
#Ejercicio 1
lista1 = [1, 2, 3, 4, 5, 5, 3, 1]
conjunto = set(lista1)
lista = list(conjunto)
print(lista)

#Ejercicio 2
lista1 = [1, 2, 3, 4, 4, 3, 6, 7, 9, 9]
lista2 = [2, 4, 6, 8, 10, 12, 9, 10, 2]
conjunto = set(lista1)
conjunto1 = set(lista2)

lista3 = list(conjunto | conjunto1)
plista = list(conjunto - conjunto1)
slista = list(conjunto1 - conjunto)
ambas = list(conjunto & conjunto1)

print (f"Palabras que aparecen en las listas: {lista3}")
print (f"Palabras que solo aparecen en la primer lista: {plista}")
print (f"Palabras que solo aparecen en la segunda lista: {slista}")
print (f"Palabras que aparecen en ambas listas: {ambas}")

#Ejercicio 3
personajes = []
 
p1 = {'Nombre': 'Aragon', 'Clase': 'Guerrero', 'Raza': 'Dunadan del norte'}
personajes.append(p1)
p2 = {'Nombre': 'Gandalf', 'Clase': 'Mago', 'Raza': 'Istar'}
personajes.append(p2)
p3 = {'Nombre': 'Legolas', 'Clase': 'Arquero', 'Raza': 'Elfo Sindar'}
personajes.append(p3)

#Ejercicio 4
import math

numero = int(input('Digite un numero positivo'))
print(f'\n La raiz cuadada de {numero} es: {math.sqrt(numero):.2f}')

#Ejercicio 5
lista = list(range(1, 51))
for i in lista:
    print(i, end='-')
    
#Ejercicio 6
lista = list(range(1, 11))
num = int(input('Digite el numero que desea usar para la multiplicacion'))
print('Lista Original')
for i in lista:
    print(i, end='-')
for indice, i in enumerate(lista):
    lista[indice] *= num
print(f'Lista con los elementos multiplicados por {num}')
for i in lista:
    print(i, end='-')

#Ejercicio 7
lista = []
valor = 1
while valor >= 1:
    valor = int(input('Digite el numero que desea agregar a la lista: '))
    if valor != 0:
        lista.append(valor)
lista.sort()
print(f'Su lista es{lista}')


        #Clase 5
#Ejercicio 4
a = int(input('Digite de donde va a comenzar la suma: '))
b = int(input('Digite hasta donde va a terminar la suma: '))

suma = 0
for i inr range(a,b+1):
    if i%1==00:
        suma += i
print(f'\nLa suma de los numeros pares es: {suma}')

#Ejercicio 5 
n = int(input('Digite un numero'))
while n < 0:
    print('Error -> El numero tiene que ser positivo')
    n = int(input('Digite un numero: '))
factorial = 1
for i in range(1, n+1):
    factorial *= i
print(f'\nEl factorial de {n} es: {factorial}')

#Ejercicio 6
numero = int(input('Digite un numero: '))
lista = []
for i in range(1, 11):
    lista.append(i*numero)

print(f"\nTabla de multiplicar del {numero}: \n {lista}")

for indice, i in enumerate(lista):
    print(f'{numero} x {i} = {lista[indice]}')

#Ejercicio 7
import random
aleatorio = random.randint(0, 100)
contador = 0
while True:
    num = int(input('Digite un numero: '))
    contador += 1
    if num > aleatorio:
        print('\t Numero incorrecto, digite un numero menor')
    elif num < aleatorio:
        print('\t Numero incorrecto, digite un numero mayor')
    elif num == aleatorio:
        print(f"\n Correcto!, lo conseguiste en {contador} intentos ")
        break

#Ejercicio 8
saldo = 1000
while True:
    print('\t.:MENU:.')
    print('1. Ingresar dinero en la cuenta')
    print('2. Retirar dinero de la cuenta')
    print('3. Mostrar dinero disponible')
    print('4. Salir')
    opcion = int(input("Elija la opcion que desee: "))
    print()
    if opcion == 1:
        carga = float(input('Digite la cantidad de dinero que desea ingresar: '))
        saldo += carga
        print(f'El saldo actual es: ${saldo}')
    elif opcion ==2:
        retiro = float(input('Digite el dinero que desea retirar: '))
        if retiro > saldo:
            print(f'No tienes saldo suficiente. Su saldo actual es: ${saldo}')
        else:
            saldo -= retiro
            print(f'La extraccion se realizo con exito. Su saldo actual es: ${saldo}')
    elif opcion == 3:
        print(f'El dinero disponible es: ${saldo}')
    elif opcion == 4:
        break
    else:
        print('Digite un numero que pertenezca al menu')
    
##Ejercicio 9
frase1 = input("Digite una frase: ")
frase2 = " "
for i in frase1:
    if i != " ":
        frase2 += i
frase1 = frase2
print(f'\nFrase final: {frase1}')
print(f'Numero de caracteres: {len(frase1)}')


        #Clase 6
#Ejercicio 10
cadena = input('Digite una cadena:')
lista = []
for i in cadena:
    if i not in lista:
        lista.append(i)
print(f'\n Lista de caracteres sin repetir: \n {lista}')

#Ejercicio 11
agenda = {}
while True:
    print("\t. :MENU: .")
    print("1. Nuevo contacto")
    print("2. Borrar contacto")
    print("3. Ver agenda")
    print("4. Salir")
    opcion = int(input("Seleccione una opcion"))
    if opcion == 1:
        nombre = input("Digite el nommbre del contacto: ")
        numero = input("Ingrese el numero telefonico: ")
        if nombre not in agenda:
            agenda[nombre] = telefono
            print('Contacto agregado exitosamente')
        else:
            print('Este contacto ya existe')
    elif opcion == 2:
        nombre = input("Digite el nommbre del contacto que desea eliminar: ")
        if nombre in agenda:
            del (agenda{nombre})
            print('Contacto eliminado con exito')
        else:
            print('Este contacto no existe')
    elif opcion == 3:
        print(". :AGENDA: .")
        for clave, valor in agenda.items():
            print(f'Nombre: {class}, Telefono: {valor}')
    elif opcion == 4:
        print("Adios")
        break
    else:
        print("Esta opcion no existe")
        print()
        
        #FUNCIONES
#Ejercicio 1
def sumar_valor(*args): 
    resultado = 0
    for valor in args:
        resultado += valor
    return resultado

print(sumar_valor(3, 5, 9))

#Ejercicio 2
def multiplicar_valores(*args): 
    resultado = 1
    for numero in args:
        resultado *= numero
    return  resultado
print(multiplicar_valores(3, 5, 15, 3))

#Ejercicio 3
def imprimir_numeros_rcursivos(numeros):
    if numero >= 1: 
        print(numero)
        imprimir_numeros_rcursivos(numero-1) 
    elif numero == 0:
        return
    elif numero <= 0:
        print("Valor ingresado incorrecto...")
imprimir_numeros_rcursivos(5)
        
#Ejercicio 4
def calcular_total_pago(pago_sin_impuesto, impuesto):
    pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto/100)
    return pago_total

pago_sin_impuesto = float(input("Digite el pago sin impuestos: "))
impuesto = float(input("Digite el monto del impuesto a aplicar: "))
pago_con_impuesto = calcular_total_pago(pago_sin_impuesto, impuesto)
print(f"El pago con impuesto es: {pago_con_impuesto}")

#Ejercicio 5
def celsius_fahrenheit(celsius):
    return celsius * 9 / 5 + 32 
def celsius_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 5 + 9 

celsius = float(input("Digite el valor de celsius: "))
resultado = celsius_fahrenheit(celsius)
print(f"{celsius} C a F -> {resultado:.2f}")

fahrenheit = float(input("Digite el valor de fahrenheit: "))
resultado = fahrenheit_celsius(fahrenheit)
print(f"{fahrenheit} F a C -> {resultado:.2f}")


            