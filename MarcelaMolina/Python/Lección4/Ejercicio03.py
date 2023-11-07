# Ejercicio 3: Insertar elementos y ordenarlos
# Pedir números y agregarlos en una listta, hasta que el usuario
# introduzca el número 0. Por último, mostrar los elem ordenados de menor a mayor

lista = []
salir = False
while not salir:
    numero = int(input('Ingrese un número: '))
    if numero == 0:
        salir = True
    else:
        lista.append(numero)
lista.sort()  #Con esta función se ordena la lista
print(f'\nLista ordenada: \n{lista}')
